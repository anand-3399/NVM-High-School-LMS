# Generated by Django 4.0.8 on 2024-02-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('SSC', 'State Board'), ('CBSC', 'CBSC Board')], max_length=25, null=True),
        ),
    ]