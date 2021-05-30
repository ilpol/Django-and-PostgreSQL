from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from users.models import User
from django.utils import timezone
import json
from django.template import loader

# Create your views here.

def index(request):
    if request.method == 'GET':
        users = User.objects.order_by('-pub_date')[:5]
        template = loader.get_template('users/index.html')
        context = {
            'users': users,
        }

        return HttpResponse(template.render(context, request))

        #return HttpResponse("template.render")
    
@csrf_exempt
def user_hobby(request, name):
    if request.method == 'GET':
        field_name = 'hobby'
        obj = User.objects.get(name=name)
        print("odj = ", obj)
        field_object = User._meta.get_field(field_name)
        print("field_object = ", field_object)
        field_value = field_object.value_from_object(obj)
        print("field_value = ", field_value)

        return HttpResponse("user: %s hobby: %s" % (name, field_value))

        #return HttpResponse("user_hobby")


@csrf_exempt
def add_users(request):
    if request.method == 'POST':
        print("request.body = ", request.body)
        dictData = json.loads(request.body)
        print("dictData = ", dictData)
        for i in dictData['objects']:
            print('i = ', i)
            new_user = User(name=i['name'], hobby=i['hobby'], pub_date=timezone.now())
            new_user.save()
           

        return HttpResponse("Users added ")
    #HttpResponse("add_users")
