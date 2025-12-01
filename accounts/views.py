import json
from django.views import View
from django.http import HttpRequest, JsonResponse
from .models import User,Profil

class AccountView(View):

    def get(self,request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body.decode())

        try:
            User.objects.get(username=data['username'])
            return JsonResponse(data={'message':'user exists'},status=400)
        except User.DoesNotExist:
            user = User(
                username = data['username'],
                password = data['password'],
                email = data.get('email'),
                phone = data.get('phone')
            )
            user.save()
            profil = Profil(user=user)
            profil.save()

            return JsonResponse(data={'message': 'now user create'},status = 201)

    def post(self,request:HttpRequest)->JsonResponse:
        pass
