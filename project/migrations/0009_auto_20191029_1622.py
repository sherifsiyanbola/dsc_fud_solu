# Generated by Django 2.2.6 on 2019-10-29 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20191029_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='progress',
            field=models.CharField(max_length=3),
        ),
    ]
