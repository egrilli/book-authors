# Generated by Django 3.2.3 on 2021-06-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(related_name='autores', to='app.Book'),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='hola', max_length=255),
        ),
    ]
