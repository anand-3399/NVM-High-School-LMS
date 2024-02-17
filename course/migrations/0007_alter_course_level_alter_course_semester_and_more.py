# Generated by Django 4.0.8 on 2024-02-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_courseoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('SSC', 'State Board'), ('CBSC', 'CBSC Board')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('First', 'First'), ('Second', 'Second')], max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.IntegerField(choices=[(2024, '2024'), (2025, '2025'), (2026, '2026')], default=0),
        ),
    ]