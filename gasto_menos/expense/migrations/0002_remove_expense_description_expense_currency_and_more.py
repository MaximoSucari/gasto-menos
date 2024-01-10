# Generated by Django 4.2.9 on 2024-01-10 13:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='description',
        ),
        migrations.AddField(
            model_name='expense',
            name='currency',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='message',
            field=models.TextField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
