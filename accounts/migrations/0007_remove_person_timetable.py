# Generated by Django 3.2.15 on 2022-10-26 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_person_timetable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='timetable',
        ),
    ]