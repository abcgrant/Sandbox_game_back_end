from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


@api_view(['POST'])
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    # print(user)
    if user:
        user = User.objects.filter(username=username)
        # print(user)
        if user is not None:
            Token.objects.update_or_create(user=user[0])
            token = Token.objects.filter(user=user[0])
            print(token)
            data = {
                'data': token[0].key
            }
            print(data)
            return Response(data)
        else:
            data = {
                'data': "用户不存在"
            }
            return Response(data)
    else:
        data = {
            'data': "用户名或密码错误"
        }
        return Response(data)


@api_view(['POST'])
def user_auto_login(request):
    token = request.POST['token']
    userToken = Token.objects.filter(key=token)
    if userToken:
        data = {
            'data': userToken[0].key
        }
        print(1,data)
        return Response(data)
    else:
        data = {
            'data': "tokenTimeout"
        }
        return Response(data)
        # user = {
        #     'token'
        # }


@api_view(['POST'])
def user_register(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
        return Response("用户已存在")
    else:
        user = User.objects.create_user(username, '', password)
        user.save()
        return Response("注册成功")


@api_view(['POST'])
def user_logout(request):
    print(request.POST)
    token = request.POST['token']
    user_token = Token.objects.get(key=token)
    user_token.delete()
    return Response('logout')

