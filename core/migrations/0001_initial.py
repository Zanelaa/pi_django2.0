# Generated by Django 4.1 on 2022-08-29 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('Quantcalorias', models.CharField(max_length=32)),
                ('quantpeso', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Cardapio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulocard', models.CharField(max_length=255)),
                ('numerorefs', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Refeicaoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloref', models.CharField(max_length=2)),
            ],
        ),
    ]
