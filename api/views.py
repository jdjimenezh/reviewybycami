from django.views.generic import ListView
from django.views import View
from django.shortcuts import render
from api.models import Post

class HomeView(ListView):
    model = Post
    template_name = "home2.html"
# Create your views here.

class GetPost(View):
    def get(self):
        p = Post.objects.get()
        respuesta ={
            'object':p
        }

        return render(self.request, 'home2.html',respuesta)