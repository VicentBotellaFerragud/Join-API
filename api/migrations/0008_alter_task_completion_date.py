# Generated by Django 4.0.4 on 2022-09-05 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_task_completion_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completion_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]