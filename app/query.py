#1) crea 5 libros con los siguientes nombres: C Sharp, Java, Python, PHP, Ruby

libro_uno =Book.objects.create(title="C Sharp", descripcion="buen libro")
libro_dos =Book.objects.create(title="Java",   descripcion="buen libro")
libro_tres =Book.objects.create(title="Python", descripcion="buen libro")
libro_cuatro =Book.objects.create(title="PHP", descripcion="buen libro")
libro_cinco =Book.objects.create(title="Ruby", descripcion="buen libro")

#2) Consulta: Crea 5 autores diferentes: Jane Austen, Emily Dickinson, Fyodor Dostoevksy, William Shakespeare, Lau Tzu

autor_uno =Author.objects.create(first_name="Jane", last_name="Austen")
autor_dos =Author.objects.create(first_name="Emily", last_name="Dickinson")
autor_tres =Author.objects.create(first_name="Fyodor", last_name="Dostoevksy")
autor_cuatro =Author.objects.create(first_name="William", last_name="Shakespeare")
autor_cinco =Author.objects.create(first_name="Lau", last_name="Tzu")


#3) Consulta: cambie el nombre del libro de C Sharp a C #

c = Book.objects.get(id=1)
c.title = "c#"
c.save()

#4) Consulta: cambie el nombre del cuarto autor a Bill

cam_a4=Author.objects.get(id=4)
cam_a4.first_name="Bill"
cam_a4.save()

#5) Consulta: Asigna el primer autor a los primeros 2 libros.

libro1= Book.objects.get(id=1) 
libro2= Book.objects.get(id=2)
autor1=Author.objects.get(id=1)

autor1.books.add(libro1)
autor1.books.add(libro2)

#6) Consulta: Asigne el segundo autor a los primeros 3 libros.

libro3= Book.objects.get(id=3)
autor2=Author.objects.get(id=2)

autor2.books.add(libro1)
autor2.books.add(libro2)
autor2.books.add(libro3)

#7) Consulta: Asigna el tercer autor a los primeros 4 libros.

libro4= Book.objects.get(id=4)
autor3=Author.objects.get(id=3)

autor3.books.add(libro1)
autor3.books.add(libro2)
autor3.books.add(libro3)
autor3.books.add(libro4)

#8) Asigne el cuarto autor a los primeros 5 libros (o en otras palabras, todos los libros)

libro5 = Book.objects.get(id=5)
autor4= Author.objects.get(id=4)

autor4.books.add(libro1)
autor4.books.add(libro2)
autor4.books.add(libro3)
autor4.books.add(libro4)
autor4.books.add(libro5)

# map(lambda l : autor4.libros.add(l), mil_libros)



#9)Consulta: recupera a todos los autores del tercer libro

autores3libro = Book.objects.get(id=3)
autores3libro.authors.all()



#10)Consulta: eliminar al primer autor del tercer libro

primer_atercer = autores3libro.authors.first()
primer_atercer.delete()


this_book_3 = Book.objects.get(id=3).authors.all()
this_author = Author.objects.get(id=1)
this_book_3.authors.remove(this_author)



#11) Consulta: Agregue el quinto autor como uno de los autores del segundo libro.

autor5=Author.objects.get(id=5)
segundo_libro= Book.objects.get(id=2)
segundo_libro.authors.add(autor5)


#12)Consulta: Encuentra todos los libros de los que el tercer autor es parte

tercer_autor= Author.objects.get(id=3)
tercer_autor.books.all()

Book.objects.filter(authors=tercer_autor.id)

#13)Consulta: Encuentra todos los autores que contribuyeron al quinto libro.

quinto_libro=Book.objects.get(id=5)

Author.objects.filter(books=quinto_libro.id)

quinto_libro.authors.all()

















