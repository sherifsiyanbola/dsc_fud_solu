# Generated by Django 2.2.7 on 2019-11-07 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_auto_20191031_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='phone',
        ),
        migrations.AlterField(
            model_name='project',
            name='submitted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
