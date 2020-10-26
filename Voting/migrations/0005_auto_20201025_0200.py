# Generated by Django 3.1.2 on 2020-10-24 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0007_auto_20201025_0140'),
        ('Voting', '0004_auto_20201024_0329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votechecksum',
            name='vote',
        ),
        migrations.AddField(
            model_name='votechecksum',
            name='team',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.team'),
        ),
    ]
