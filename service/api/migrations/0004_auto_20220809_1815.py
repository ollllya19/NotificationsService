# Generated by Django 3.2.15 on 2022-08-09 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220807_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='filter',
            field=models.CharField(default='987', max_length=3),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_code',
            field=models.CharField(max_length=3),
        ),
    ]
