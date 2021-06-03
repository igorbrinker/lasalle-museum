# Generated by Django 3.2.3 on 2021-06-02 12:26

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materials', '0004_alter_materials_description'),
        ('collection', '0002_auto_20210602_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artifacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('slug', models.SlugField(default='', unique=True)),
                ('description', models.CharField(default='', max_length=200)),
                ('author', models.CharField(default='Desconhecido', max_length=50)),
                ('about', ckeditor.fields.RichTextField(blank=True)),
                ('usage', models.CharField(default='Desconhecido', max_length=60)),
                ('style', models.CharField(default='Desconhecido', max_length=30)),
                ('culture', models.CharField(default='Desconhecida', max_length=30)),
                ('ethnicity', models.CharField(default='Desconhecida', max_length=30)),
                ('age', models.CharField(default='Desconhecido', max_length=12)),
                ('inscriptions', models.CharField(default='Desconhecido', max_length=200)),
                ('fabrication_date', models.CharField(default='Desconhecido', max_length=12)),
                ('heritage_id', models.CharField(default='', max_length=30, unique=True)),
                ('manufacture', models.CharField(default='Desconhecida', max_length=30)),
                ('decoration', models.CharField(default='Desconhecida', max_length=30)),
                ('length', models.FloatField(default=0, max_length=5)),
                ('width', models.FloatField(default=0, max_length=5)),
                ('diameter', models.FloatField(default=0, max_length=5)),
                ('height', models.FloatField(default=0, max_length=5)),
                ('circumference', models.FloatField(default=0, max_length=5)),
                ('depth', models.FloatField(default=0, max_length=5)),
                ('weight', models.FloatField(default=0, max_length=5)),
                ('owner', models.CharField(default='Desconhecido', max_length=30)),
                ('acqusition_date', models.CharField(default='Desconhecido', max_length=12)),
                ('donor', models.CharField(default='Desconhecido', max_length=30)),
                ('last_owner', models.CharField(default='Desconhecido', max_length=30)),
                ('personality', models.CharField(default='Desconhecido', max_length=30)),
                ('image', models.ImageField(default='', upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('collection', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='collection', to='collection.collection')),
                ('material', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='material', to='materials.materials')),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
