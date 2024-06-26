# Generated by Django 4.1 on 2024-05-13 08:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_comment_created_date_alter_post_created_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="post",
            name="published_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
