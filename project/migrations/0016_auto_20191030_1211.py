# Generated by Django 2.2.6 on 2019-10-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20191030_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='progress',
            field=models.CharField(default=0, max_length=3, verbose_name='progress(%)'),
        ),
    ]
