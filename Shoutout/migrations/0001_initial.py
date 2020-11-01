# Generated by Django 3.1.2 on 2020-10-26 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoutout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('emp_appreciated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.emp')),
                ('emp_appreciator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='shoutoutlikes', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, default='', null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('emp_commented', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='commentlikes', to=settings.AUTH_USER_MODEL)),
                ('shoutout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shoutout.shoutout')),
            ],
        ),
    ]
