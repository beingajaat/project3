from django.shortcuts import render
from django.views import generic
from .models import blog

class BlogList(generic.ListView):
    queryset = blog.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'

class BlogDetail(generic.DetailView):
    model = blog
    template_name = 'blog_details.html'
    
# Create your views here.
