# Generated by Django 3.0.1 on 2020-01-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Internships', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
