from tkinter.messagebox import NO
from django.shortcuts import render
from django.views.generic import *
from django.http import JsonResponse
from crud_ajax.models import Conta
# Create your views here.

class IndexView(TemplateView):
    template_name = 'crud_ajax/base.html'


class ContaView(ListView):
    model = Conta
    template_name = 'crud_ajax/crud.html'
    context_object_name = 'conta'


class CreateConta(View):
    def get (self,request):
        desc1  = request.GET.get('desc', None)
        fornecedor1 = request.GET.get('fornecedor', None)


        obj = Conta.objects.create(
            desc = desc1,
            fornecedor = fornecedor1
        )

        user = {'id':obj.id,'desc':obj.desc,'fornecedor':obj.fornecedor}

        data = {
            'user': user
        }

        return JsonResponse(data)