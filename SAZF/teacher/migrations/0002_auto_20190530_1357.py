# Generated by Django 2.2.1 on 2019-05-30 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='age_of_enter',
            field=models.DateField(null=True),
        ),
    ]
