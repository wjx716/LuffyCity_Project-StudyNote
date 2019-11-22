# Generated by Django 2.2.6 on 2019-11-07 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20191105_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='pid',
            field=models.ForeignKey(blank=True, help_text='对于非菜单权限需要选择一个可以称为菜单的权限，用户做默认展开和选择菜单', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='rbac.Permission', verbose_name='关联的权限'),
        ),
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='rbac.Permission', verbose_name='拥有的所有权限'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='roles',
            field=models.ManyToManyField(blank=True, to='rbac.Role', verbose_name='拥有的所有角色'),
        ),
    ]