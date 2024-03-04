# Generated by Django 5.0.2 on 2024-03-04 06:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("robot_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="name",
        ),
        migrations.AlterField(
            model_name="testuser",
            name="feeling",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="testuser",
            name="score",
            field=models.FloatField(max_length=10, null=True),
        ),
    ]
