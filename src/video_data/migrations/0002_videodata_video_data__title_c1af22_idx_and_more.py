# Generated by Django 4.0.2 on 2022-02-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_data', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='videodata',
            index=models.Index(fields=['title', 'description'], name='video_data__title_c1af22_idx'),
        ),
        migrations.AddIndex(
            model_name='videodata',
            index=models.Index(fields=['description'], name='video_data__descrip_d65777_idx'),
        ),
        migrations.AddIndex(
            model_name='videodata',
            index=models.Index(fields=['title'], name='video_data__title_7e6292_idx'),
        ),
    ]
