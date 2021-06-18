from django.shortcuts import render, HttpResponse,redirect
from app.models import Book, Author

def index(request):
    context = {
        "authors": Author.objects.all(),
        "books": Book.objects.all(),
    }
    return render(request,"index.html",context)

def author(request):
    context = {
        "authors": Author.objects.all(),
    }
    return render(request,"authors.html",context)

def agregar_autor(request):
    Author.objects.create(first_name=request.POST['autor'])
    return redirect("/app/authors")

def agregar_libro(request):
    Book.objects.create(title=request.POST['libro'], descripcion=request.POST['descripcion'])
    return redirect("/app")

def ver_libro(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method=="GET":
        autor=book.authors.all()
        todos_autores=Author.objects.all()
        context={
            'books': book,
            'autores':autor,
            'todos_autores':todos_autores
        }
        return render(request,'view_book.html',context)
    
    if request.method=="POST":
        print(request.POST)
        book.authors.add(request.POST['autorNuevo'])
        return redirect('/app/books/'+book_id)


def ver_autor(request,author_id):
    autor=Author.objects.get(id=author_id)
    if request.method=="GET":
        book=autor.books.all()
        todos_libros=Book.objects.all()
        context={
            'books': book,
            'autores':autor,
            'todos_libros':todos_libros
        }
        return render(request,'view_author.html',context )

    if request.method=="POST":
        print(request.POST)
        autor.books.add(request.POST['libroNuevo'])
        return redirect('/app/authors/'+author_id)

'''
def autor_agregarLibro(request,author_id):
    autor=Author.objects.get(id=author_id)
    autor.books.add(request.POST['libroNuevo'])
    return redirect('authors/<author_id>')
'''



