# Generated by Django 3.0.7 on 2020-06-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20200615_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='otp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]