# Generated by Django 4.2.5 on 2024-02-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_univcab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='diplom',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='passport',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
