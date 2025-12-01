from django.urls import path
from .views import AccountView

urlpatterns = [
    path('',AccountView.as_view(),name='accounts')      # as_view clasni funtionga aylantirib beradi
]
