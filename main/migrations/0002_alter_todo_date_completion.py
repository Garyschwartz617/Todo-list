# Generated by Django 3.2.6 on 2021-08-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_completion',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]