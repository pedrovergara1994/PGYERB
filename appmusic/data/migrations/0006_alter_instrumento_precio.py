# Generated by Django 4.2.2 on 2023-06-21 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_instrumento_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumento',
            name='precio',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
