# Generated by Django 4.2.9 on 2024-01-10 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
        ),
    ]
