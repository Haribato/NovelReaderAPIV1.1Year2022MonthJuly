# Generated by Django 4.0.5 on 2022-07-01 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='chapters',
            name='likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='books',
            name='authors',
            field=models.ManyToManyField(to='books.author'),
        ),
        migrations.AddField(
            model_name='books',
            name='book_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.source'),
        ),
        migrations.AddField(
            model_name='books',
            name='book_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.status'),
        ),
        migrations.AddField(
            model_name='books',
            name='categories',
            field=models.ManyToManyField(to='books.category'),
        ),
        migrations.AddField(
            model_name='books',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.language'),
        ),
    ]