# Generated by Django 4.1.1 on 2022-09-13 12:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog_app', '0002_alter_post_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]