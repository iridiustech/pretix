# Generated by Django 3.2.4 on 2021-09-15 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixapi', '0006_alter_webhook_target_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webhookcall',
            name='target_url',
            field=models.URLField(max_length=255),
        ),
    ]
