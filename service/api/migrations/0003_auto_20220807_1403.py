# Generated by Django 3.2.15 on 2022-08-07 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='client_id',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='mailing_id',
            new_name='mailing',
        ),
    ]