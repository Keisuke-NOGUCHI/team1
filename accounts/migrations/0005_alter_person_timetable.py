# Generated by Django 3.2.15 on 2022-10-26 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20221026_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='timetable',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.timetable', verbose_name='時間割'),
        ),
    ]