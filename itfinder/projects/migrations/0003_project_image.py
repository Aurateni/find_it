# Generated by Django 4.0.6 on 2022-07-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_total_votes_project_votes_ratio_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='project_images/default.jpg', null=True, upload_to='project_images'),
        ),
    ]
