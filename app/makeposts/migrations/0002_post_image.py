# Generated by Django 3.0.2 on 2020-02-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeposts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
