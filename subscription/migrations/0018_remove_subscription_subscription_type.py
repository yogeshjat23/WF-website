# Generated by Django 3.1.1 on 2020-11-29 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0017_managesubscriptionpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='subscription_type',
        ),
    ]