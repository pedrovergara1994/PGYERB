# Generated by Django 4.2.2 on 2023-06-23 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_alter_instrumento_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumento',
            name='img',
            field=models.TextField(blank=True, null=True),
        ),
    ]
