from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *





class ReportCreate(APIView):
    def post(self, request, format=None):
        user = User.objects.filter(username=request.user)
        payload = request.data
        payload['author'] = user[0].id
        serializer = ReportSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportList(APIView):
    def get(self, request):
        reports = Report.objects.all()
        data = ReportListSerializer(reports, many=True).data
        return Response({"reports": data}, status=200)


class LikeView(APIView):
    lookup_url_kwarg = 'id'

    def get(self, request):
        id = request.GET.get(self.lookup_url_kwarg)
        post = Report.objects.get(id=id)
        post.likes.add(request.user)
        return Response({'result':'The post was successfully liked!'})


class UnlikeView(APIView):
    lookup_url_kwarg = 'id'

    def get(self, request):
        id = request.GET.get(self.lookup_url_kwarg)
        post = Report.objects.get(id=id)
        post.likes.remove(request.user)
        return Response({'result':'Like has been successfully removed from the post!'})


class ReportCreateViewSet(viewsets.GenericViewSet):
    permission_classes = None
    queryset = Report.objects.all()
    pagination_class = None
    permission_class = None

    # def list(self, request):
    #     queryset = Report.objects.all()
    #     page = self.paginate_queryset(queryset)
    #     serializer = ReportSerializer(page, many=True)
    #     return self.get_paginated_response(serializer.data)
    def create(self, request):
        serializer = ReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)

        return

    # def list(self, request):
    #     pass

        # user = serializer.validated_data["usuario"]
        # django_login(request, user)
        # token, created = Token.objects.get_or_create(user=user)
        # return Response({"token": token.key}, status=200)

    @action(methods=['GET'], detail=False)
    def post_file(self, request, *args, **kwargs):
        print('Beket')
        post = self.queryset()
        print(post)
        return
