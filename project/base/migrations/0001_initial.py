# Generated by Django 4.1.2 on 2022-10-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noteTitle', models.CharField(max_length=30)),
                ('noteDesc', models.TextField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]