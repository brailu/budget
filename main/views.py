from contextlib import redirect_stderr
from django.template.response import TemplateResponse
from django.views import View
from django.shortcuts import render, redirect

from main.forms import CategoryCreateForm


class HelloView(View):

    def get(self, request):
        return TemplateResponse(request, 'main/hello.html')


def category_create_view(request):
    
    if request.method == 'GET':
        category_create_form = CategoryCreateForm()
        return render(request, 'main/account/<id>/category.html', {'form': category_create_form})

    if request.method == 'POST':
        category_create_form = CategoryCreateForm(request.Post)
        if category_create_form.is_valid():
            category_create_form.save()
            return redirect('/account/category/')
        else:
            return render(request, 'main/account/<id>/category.html', {'form': category_create_form})

