from django.urls import path
from galeria.views import index,imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name = 'imagem'),
]
#pode adicionar mais urls que estão ligadas ao app galeria, isolando as urls

