from tkinter.messagebox import NO
from django.shortcuts import render
from django.views.generic import *
from django.http import JsonResponse
from matplotlib.artist import Artist
from crud_ajax.models import Conta, Album
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

class AlbumView(ListView):
    model = Album
    template_name = 'crud_ajax/album.html'
    context_object_name = 'album'

class CreateAlbum(View):
    def get (self,request):
        name1  = request.GET.get('name', None)
        artist1 = request.GET.get('artist', None)
        num_stars1 = request.GET.get('num_stars', None)



        obj = Album.objects.create(
            name = name1,
            artist = artist1,
            num_stars = num_stars1
        )

        user = {'id':obj.id,'name':obj.name,'artist': obj.artist,'num_stars': obj.num_stars}

        data = {
            'user': user
        }

        return JsonResponse(data)
        
