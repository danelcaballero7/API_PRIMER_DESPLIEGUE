# Generated by Django 4.1.1 on 2022-09-21 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='resumen',
            new_name='resume',
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='titulo',
            new_name='title',
        ),
    ]