# Generated by Django 3.1.4 on 2021-05-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_staff_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile.jpg', null=True, upload_to=''),
        ),
    ]
