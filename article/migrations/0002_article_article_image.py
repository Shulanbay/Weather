# Generated by Django 2.2.6 on 2019-12-10 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Images'),
        ),
    ]