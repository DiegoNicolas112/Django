# Generated by Django 5.1.7 on 2025-05-03 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartphone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturers',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
