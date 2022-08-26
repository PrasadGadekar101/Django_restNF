import email
from django.http import JsonResponse
from .models import User

# Create your views here.

def users_home(request):
    all_user = User.objects.get(email='prasad@gmail.com')
    print(all_user)
    user = {'first_name':all_user.first_name, 'last_name': all_user.last_name}
    return JsonResponse(data=user)

def user_details(request,pk):
    user_details = User.objects.get(id=pk)
    user = {'first_name':user_details.first_name, 'last_name': user_details.last_name}
    return JsonResponse(data=user)