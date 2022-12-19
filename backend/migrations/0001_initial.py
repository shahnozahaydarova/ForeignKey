# Generated by Django 3.2.16 on 2022-12-16 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contant', models.CharField(max_length=250)),
                ('data', models.DateField(auto_now_add=True)),
                ('img', models.CharField(max_length=255)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.name')),
            ],
        ),
    ]
