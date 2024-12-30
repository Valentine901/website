# Generated by Django 5.1.4 on 2024-12-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_me_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_image', models.ImageField(default='default', upload_to='media')),
                ('card_image', models.ImageField(default='default', upload_to='media')),
                ('web_image', models.ImageField(default='default', upload_to='media')),
                ('link_tag', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]