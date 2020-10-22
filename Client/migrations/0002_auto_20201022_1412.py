# Generated by Django 3.1.2 on 2020-10-22 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='emp',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='team',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Client.team'),
        ),
        migrations.AlterField(
            model_name='child',
            name='emp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.emp', unique=True),
        ),
        migrations.RemoveField(
            model_name='child',
            name='parent',
        ),
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ManyToManyField(to='Client.Parent'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('after_deadline', models.BooleanField(default=False)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.child')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.project')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.team')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=100)),
                ('confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='emp',
            name='organization',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Client.organization'),
        ),
    ]