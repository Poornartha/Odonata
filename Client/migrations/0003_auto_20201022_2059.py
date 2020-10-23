# Generated by Django 3.1.2 on 2020-10-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0002_auto_20201022_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='file_project',
        ),
        migrations.AddField(
            model_name='project',
            name='project_create_file',
            field=models.FileField(blank=True, null=True, upload_to='project_create/'),
        ),
        migrations.AddField(
            model_name='submission',
            name='file_project',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]