from django.urls import path
from main.views import (
    HelloView,
    category_create_view,


)

urlpatterns = [
    path('', HelloView.as_view(), name='hello_view'),
    path('main/account/<id>/category.html', category_create_view)
]
