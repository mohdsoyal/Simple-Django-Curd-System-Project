# Generated by Django 5.0.1 on 2024-01-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.CharField(max_length=20),
        ),
    ]
