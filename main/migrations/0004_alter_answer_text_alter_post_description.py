# Generated by Django 4.1.1 on 2022-09-24 19:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_post_image_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
