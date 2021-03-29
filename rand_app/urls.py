from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('generate', views.generate),
    path('random_word', views.random_word)
    # path('admin/', admin.site.urls),
]