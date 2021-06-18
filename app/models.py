from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255,null=False )
    descripcion =  models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #authors=   
    def __repr__(self):
        return f"< Libros: Titulo = {self.title}, Descripcion= {self.descripcion}>"

class Author(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=True)
    books = models.ManyToManyField(Book, related_name="authors")
    notas = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"< Autor: Nombre = {self.first_name}, Apellido = {self.last_name}, Notas = {self.notas} >"