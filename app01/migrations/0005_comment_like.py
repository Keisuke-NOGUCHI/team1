<<<<<<< HEAD
# Generated by Django 4.1.3 on 2022-12-06 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_comment_anonymity_comment_image_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
=======
# Generated by Django 4.1.3 on 2022-12-06 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_comment_anonymity_comment_image_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
>>>>>>> 683c62027f48aa9bf47b0f120fd8de83e3ec9b10
