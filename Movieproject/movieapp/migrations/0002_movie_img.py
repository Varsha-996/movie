# Generated by Django 4.1.7 on 2023-03-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='varyasha', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
