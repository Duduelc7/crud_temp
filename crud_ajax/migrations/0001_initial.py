# Generated by Django 4.1.2 on 2022-10-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=200, verbose_name='Descrição')),
                ('fornecedor', models.CharField(max_length=255)),
            ],
        ),
    ]
