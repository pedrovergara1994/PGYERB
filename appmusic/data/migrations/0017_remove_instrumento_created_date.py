# Generated by Django 4.2.2 on 2023-06-23 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0016_remove_carrito_user_carrito_cliente_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrumento',
            name='created_date',
        ),
    ]
