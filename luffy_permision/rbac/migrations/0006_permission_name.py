# Generated by Django 2.2.6 on 2019-11-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0005_auto_20191107_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='URL别名'),
        ),
    ]