# Generated by Django 4.1.3 on 2022-11-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0007_alter_todo_createdat_alter_todo_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='CreatedAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
