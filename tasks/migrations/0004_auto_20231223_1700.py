# Generated by Django 3.2.17 on 2023-12-23 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20231223_1249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['user_id'], 'verbose_name': 'Todo Task'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]
