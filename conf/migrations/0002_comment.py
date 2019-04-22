# Generated by Django 2.2 on 2019-04-21 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Comment text')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('moder', models.BooleanField(default=False, verbose_name='Moderation')),
                ('conf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conf.Conference', verbose_name='Conference')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'db_table': 'comments',
            },
        ),
    ]
