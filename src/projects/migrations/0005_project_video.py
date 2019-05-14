# Generated by Django 2.1.7 on 2019-03-25 13:07

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=projects.models.upload_video_path),
        ),
    ]
