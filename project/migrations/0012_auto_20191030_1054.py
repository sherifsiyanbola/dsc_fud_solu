# Generated by Django 2.2.6 on 2019-10-30 09:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20191029_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='progress_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='progress',
            field=models.CharField(default=0, max_length=3, verbose_name='progress(%)'),
        ),
    ]
