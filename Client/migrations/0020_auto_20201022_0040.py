# Generated by Django 3.1.2 on 2020-10-21 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0019_auto_20201022_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='emp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.emp', unique=True),
        ),
    ]
