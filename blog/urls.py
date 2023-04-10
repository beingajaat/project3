from . import views
from django.urls import path

urlspatterns = [
    path('',views.BlogList.as_view(), name='home'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name = 'blog_detail')
]