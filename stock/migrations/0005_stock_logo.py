# Generated by Django 3.2.8 on 2021-12-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20211114_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
