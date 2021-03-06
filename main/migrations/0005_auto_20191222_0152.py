# Generated by Django 2.2.6 on 2019-12-21 20:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_userprofile_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='file_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='file',
            field=models.FileField(blank=True, upload_to='profile_image'),
        ),
    ]
