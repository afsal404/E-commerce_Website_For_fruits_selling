# Generated by Django 4.2.4 on 2023-10-04 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0002_alter_catdata_cat_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catdata',
            old_name='cat_image',
            new_name='cat_img',
        ),
    ]