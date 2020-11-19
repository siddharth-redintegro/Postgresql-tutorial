from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Blog,User
from django.core import serializers
from django.utils import timezone
import json
from django.views.decorators.http import require_http_methods 
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World")

def users_list(request):
    data=[
        {
            'name':'Sid'
        }
    ]
    return JsonResponse(data,safe=False)

def insert_user(request):
    data = json.loads(request.body.decode('utf-8'))
    return JsonResponse(data,safe=False)

def blog_list(request):
    data = Blog.objects.all()
    response = serializers.serialize('json',data)
    return HttpResponse(response,content_type='application/json')

@csrf_exempt
@require_http_methods(['POST'])
def insert_blog(request):
    data = json.loads(request.body.decode('utf-8'))

    new_blog = Blog(
        name=data['name'],
        id = data['id'],
        description = data['description'],
        posted_by=data['posted_by'],
        posted_on=timezone.now()
    )

    new_blog.save()

    return JsonResponse(data)

def delete_blog(request,description):
    data = json.loads(request.body.decode('utf-8'))
    old_blog = Blog.objects.get(pk=id)

    old_blog.description = data.description
    
    old_blog.delete()

    return JsonResponse(data)

def update_blog(request,id):
    data = json.loads(request.body.decode('utf-8'))

    old_blog = Blog.objects.get(pk=id)

    old_blog.description = data.description
    old_blog.name = data.name
    old_blog.posted_on = timezone.now()

    
    return JsonResponse(data)

@csrf_exempt
@require_http_methods(['POST'])
def inser_new_user(request):
    data = json.loads(request.body.decode('utf-8'))

    new_user = User(
        user_name=data['user_name'],
        user_desc=data['user_desc'],
        user_phone=data['user_phone'],
        user_email=data['user_email'],
        user_password=data['user_password']
    )
    new_user.save()
    return JsonResponse(data)
    

@csrf_exempt
@require_http_methods(['POST'])
def update_user(request, id):
    data = json.loads(request.body.decode('utf-8'))
    old_user = User.objects.get(pk=id)

    old_user.user_name = data['user_name']
    old_user.user_desc = data['user_desc']
    old_user.user_phone = data['user_phone']
    old_user.user_email=data['user_email']
    old_user.user_password=data['user_password']
    old_user.save()
    return JsonResponse(data)



@csrf_exempt
@require_http_methods(['POST'])
def delete_user(request,id):
    print(id)
    old_user = User.objects.get(pk=id)
    old_user.delete()
    return HttpResponse(f'ID deleted: {id}')

def user_list(request):
    data = User.objects.all()
    response = serializers.serialize("json", data)
    return HttpResponse(response, content_type="application/json")