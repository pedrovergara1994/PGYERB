# Generated by Django 4.2.2 on 2023-06-21 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_rename_user_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumento',
            name='precio',
            field=models.IntegerField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
