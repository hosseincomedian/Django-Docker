# Generated by Django 3.2.19 on 2023-06-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0005_profile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="is_superusername",
            new_name="is_verified",
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]
