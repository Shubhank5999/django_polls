# Generated by Django 5.1.4 on 2024-12-28 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='Question',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='pub_dat',
            new_name='pub_date',
        ),
    ]
