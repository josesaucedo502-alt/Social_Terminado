# Generated by Django 3.1.7 on 2021-03-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='image',
            field=models.ImageField(default='info.png', upload_to=''),
        ),
    ]