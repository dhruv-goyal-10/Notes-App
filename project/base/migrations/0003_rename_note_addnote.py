# Generated by Django 4.1.2 on 2022-10-20 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_note_delete_notes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='Addnote',
        ),
    ]