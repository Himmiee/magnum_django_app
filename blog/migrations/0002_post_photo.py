# Generated by Django 4.0.6 on 2022-07-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank='true', null='true', upload_to='pics'),
            preserve_default='true',
        ),
    ]
