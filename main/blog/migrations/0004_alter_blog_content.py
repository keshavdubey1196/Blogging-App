# Generated by Django 4.1.7 on 2023-03-09 19:15

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_remove_blog_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="content",
            field=froala_editor.fields.FroalaField(default=None),
        ),
    ]