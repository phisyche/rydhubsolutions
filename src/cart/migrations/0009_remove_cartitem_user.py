# Generated by Django 2.2.9 on 2020-01-29 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_cartitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='user',
        ),
    ]
