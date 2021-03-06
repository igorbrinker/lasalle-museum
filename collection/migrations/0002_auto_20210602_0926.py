# Generated by Django 3.2.3 on 2021-06-02 12:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='collection_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='collection_description',
        ),
        migrations.AddField(
            model_name='collection',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
