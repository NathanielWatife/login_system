# Generated by Django 4.2.7 on 2023-11-20 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_profielimg_userprofile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
