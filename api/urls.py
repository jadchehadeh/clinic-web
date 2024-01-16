from django.urls import path
from .views import UserGetCreate

urlpatterns=[
    path('getuser/',UserGetCreate.as_view(),name='UserGetCreate'),
]

