# Generated by Django 4.2.4 on 2023-10-04 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0003_rename_cat_image_catdata_cat_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catdata',
            old_name='cat_img',
            new_name='image',
        ),
    ]