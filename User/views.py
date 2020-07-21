from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from User.models import User


class Login(APIView):
    def get(self, request):
        username = request.session.get('username')
        if username:
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'login.html')

    @csrf_exempt
    def post(self, request):
        u_name = request.data.get('username')
        u_password = request.data.get('password')
        try:
            user = User.objects.get(username=u_name)
            if user.password == u_password:
                request.session['username'] = 'username'
                return HttpResponseRedirect(reverse('index'))
            return Response(data='密码错误')

        except:
            return Response(data='不存在用户')


class QQlogin(APIView):
    def get(self, request):
        return Response(data='正在施工中.......')

    def post(self, request):
        pass


class Register(APIView):
    def get(self, request):
        return render(request, '../static/../templates/register.html')

    @csrf_exempt
    def post(self, request):
        pass


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('login'))


