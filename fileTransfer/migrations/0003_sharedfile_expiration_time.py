# Generated by Django 4.2.7 on 2023-11-11 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileTransfer', '0002_sharedfile_shareable_link_alter_sharedfile_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharedfile',
            name='expiration_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]