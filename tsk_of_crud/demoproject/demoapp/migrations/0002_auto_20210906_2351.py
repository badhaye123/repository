# Generated by Django 3.2.6 on 2021-09-06 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='laptopcompanyname',
            new_name='lapcompanyname',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='laptopmodelname',
            new_name='lapmodelname',
        ),
    ]