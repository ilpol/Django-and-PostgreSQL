# Generated by Django 3.2.3 on 2021-05-23 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(default='', max_length=200)),
                ('users', models.CharField(default='', max_length=200)),
                ('messages', models.CharField(default='', max_length=200)),
            ],
        ),
    ]