# Generated by Django 5.1.4 on 2025-01-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=2500, unique_for_date='publish'),
        ),
    ]
