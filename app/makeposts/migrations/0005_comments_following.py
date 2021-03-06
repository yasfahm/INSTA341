# Generated by Django 2.2.3 on 2020-02-22 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('makeposts', '0004_auto_20200205_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('commenter', models.IntegerField()),
                ('comment_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('comment', models.TextField()),
                ('username', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('follower', models.IntegerField()),
            ],
            options={
                'db_table': 'following',
                'unique_together': {('user_id', 'follower')},
            },
        ),
    ]
