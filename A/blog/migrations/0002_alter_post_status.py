# Generated by Django 5.1.4 on 2025-01-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('DF', 'DRAFT'), ('PB', 'PUBLISHED')], default='DF', max_length=2),
        ),
    ]
