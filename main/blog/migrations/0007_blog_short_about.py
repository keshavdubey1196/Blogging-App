# Generated by Django 4.1.7 on 2023-03-12 16:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_blog_count_blog_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="short_about",
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]