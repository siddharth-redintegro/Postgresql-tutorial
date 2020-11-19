from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Blog
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



