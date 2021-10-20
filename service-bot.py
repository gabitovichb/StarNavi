import requests, json, random, string, ast, time


def main():
    #Пути для запроса
    BASE_URL = 'http://127.0.0.1:8000'
    BASE_AUTH = 'auth'
    BASE_POST = 'post'


    #Открываем файл для использования параметров
    with open('./rules.json', 'r') as read_file:
        bot = json.load(read_file)
    

    #Для рандомного генератора текста
    letters = [string.ascii_lowercase,
                    string.ascii_uppercase, string.ascii_letters,
                    string.digits]
    
    for test in range(bot['number_of_users']):
        #Создаем рандомные данные для теста
        username = '123abc' + ''.join(random.choice(letters[0]) for x in range(5))
        email = '123xzv' + ''.join(random.choice(letters[0]) for x in range(5)) + "@gmail.com"
        password = ''.join(random.choice(letters[0]) for x in range(5)) + '@X12cx'


        #Тестинг регистрации пользователя
        url = BASE_URL + '/' + BASE_AUTH + '/' + 'signup' + '/'
        data = {
            "username": username,
            "email": email,
            "password": password 
        }
        result = requests.post(url, data=data)
        print('The user was successfully created!')



        #Тестинг авторизации пользователя
        url = BASE_URL + '/' + BASE_AUTH + '/' + 'login' + '/'
        data = {
            "username": username,
            "password": password 
        }
        result = requests.post(url, data=data).text
        result = ast.literal_eval(result)
        token = 'JWT ' + result['token']
        user_id = result['id']
        headers = {'Authorization': '{}'.format(token)}


        #Тестинг создание поста
        post_id = []
        for test1 in range(bot['max_posts_per_user']):
            #Генерируем текст и название для поста
            text = []
            for j in range(2):
                temp = ''
                for k in letters:
                    temp += ( ''.join(random.choice(k) for i in range(3)) )
                    temp += ( ''.join(random.choice(string.punctuation) for i in range(1)) )
                text.append(temp)
            title = text[0]
            body = text[1]


            url = BASE_URL + '/' + BASE_POST + '/' + 'create'
            data = {
                "title": title,
                "body": body,
                "author": user_id
            }
            result = requests.post(url, headers=headers, data=data).text
            result = ast.literal_eval(result)
            post_id.append(result['id'])
            print('The post was successfully created!')


        #Тестинг лайк поста
        for test2 in range(bot['max_likes_per_user']):
            url = BASE_URL + '/' + BASE_POST + '/' + 'like'
            data = {
                "like_post": post_id[test2],
                "like_author": user_id,
                "like": 1
            }
            result = requests.post(url, headers=headers, data=data)
            print('The like has already been set!')
        time.sleep(5)
    print('The bot has successfully completed its verification!')


if __name__ == '__main__':
    main()