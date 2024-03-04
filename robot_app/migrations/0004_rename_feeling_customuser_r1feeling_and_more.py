# Generated by Django 5.0.2 on 2024-03-04 08:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("robot_app", "0003_customuser_feeling_customuser_score_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customuser",
            old_name="feeling",
            new_name="r1feeling",
        ),
        migrations.RenameField(
            model_name="customuser",
            old_name="score",
            new_name="r1score",
        ),
        migrations.AddField(
            model_name="customuser",
            name="r2feeling",
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="r2score",
            field=models.FloatField(default=None, max_length=10, null=True),
        ),
    ]
