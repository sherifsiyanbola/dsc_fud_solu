# Generated by Django 2.1.7 on 2019-04-03 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_project_budget_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]
