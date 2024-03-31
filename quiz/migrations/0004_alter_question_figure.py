# Generated by Django 4.0.8 on 2024-03-31 08:08

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_quiz_single_attempt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='figure',
            field=models.ImageField(blank=True, null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='uploads/%Y/%m/%d', verbose_name='Figure'),
        ),
    ]