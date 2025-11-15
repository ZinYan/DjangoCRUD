from django.urls import path
from .views import *
urlpatterns = {
    path("",posts_list),
    path("<int:pk>/",posts_read),
    path("create/", posts_create),
}