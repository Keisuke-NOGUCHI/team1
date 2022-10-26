# Generated by Django 3.2.15 on 2022-10-26 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_person_timetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='timetable',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.timetable', verbose_name='時間割'),
        ),
    ]