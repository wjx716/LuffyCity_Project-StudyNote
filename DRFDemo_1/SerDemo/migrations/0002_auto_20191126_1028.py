# Generated by Django 2.2.6 on 2019-11-26 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SerDemo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publiser',
            new_name='publisher',
        ),
    ]