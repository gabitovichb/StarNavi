from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Report, Like, Dislike
from authorize.models import User
from .serializers import ReportSerializer, ReportListSerializer, LikeSerializer, DislikeSerializer
from django.db.models import Q
from rest_framework.permissions import AllowAny



class ReportCreate(APIView):
    serializer_class = ReportSerializer


    def post(self, request):
        user = User.objects.filter(username=request.user)
        payload = request.data
        payload['author'] = user[0].id
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportList(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ReportListSerializer

    def get(self, request):
        reports = Report.objects.all()
        data = self.serializer_class(reports, many=True).data
        return Response({"reports": data}, status=200)


class LikeView(APIView):
    serializer_class = LikeSerializer

    def post(self, request):
        payload = request.data
        result = Like.objects.filter(Q(like_post=payload['like_post']) & Q(like_author=request.user))
        if len(result) == 0:
            user = User.objects.filter(username=request.user)
            payload['like_author'] = user[0].id
            payload['like'] = 1
            serializer = self.serializer_class(data=payload)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message":"The like has already been set!"}, status=status.HTTP_200_OK)


class UnlikeView(APIView):
    serializer_class = DislikeSerializer

    def post(self, request):
        payload = request.data
        result = Dislike.objects.filter(Q(dislike_post=payload['dislike_post']) & Q(dislike_author=request.user))
        if len(result) == 0:
            user = User.objects.filter(username=request.user)
            payload['dislike_author'] = user[0].id
            payload['dislike'] = 1
            serializer = self.serializer_class(data=payload)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message":"The dislike has already been set!"}, status=status.HTTP_200_OK)



class PostAnaliticsLikesView(APIView):
    serializer_class = LikeSerializer

    def get(self, request):
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        likes_analitic = Like.objects.filter(like_created__range=[date_from, date_to])
        if len(likes_analitic) > 0:
            return Response({'likes by period': len(likes_analitic)})
        else:
            return Response({'likes by period': 0})
