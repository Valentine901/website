# Generated by Django 5.1.4 on 2024-12-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(null=True)),
                ('username', models.CharField(max_length=200, null=True)),
                ('job', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
