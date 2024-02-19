# Generated by Django 4.1.9 on 2024-02-16 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0002_blog_otpverification_delete_about_delete_awards_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="SaveBlog",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("Post_id", models.UUIDField()),
                (
                    "updated_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "User",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comments",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("Post_id", models.UUIDField()),
                ("category", models.CharField(max_length=50)),
                ("comment", models.CharField(max_length=400)),
                ("last_updated_date", models.DateTimeField(auto_now=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
