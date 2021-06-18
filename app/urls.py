from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('authors',views.author),
    path('add-author',views.agregar_autor),
    path('add-book',views.agregar_libro),
    path('books/<book_id>',views.ver_libro),
    path('authors/<author_id>',views.ver_autor),
    

]