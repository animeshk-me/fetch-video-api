# Generated by Django 4.0.2 on 2022-02-07 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_data', '0002_videodata_video_data__title_c1af22_idx_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='videodata',
            name='video_data__title_7e6292_idx',
        ),
    ]