# Generated by Django 5.1.4 on 2024-12-30 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='me',
            name='year',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
