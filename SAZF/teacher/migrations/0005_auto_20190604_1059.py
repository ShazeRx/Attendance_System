# Generated by Django 2.2.1 on 2019-06-04 08:59

from django.db import migrations
import teacher.managers


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20190604_1054'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='teacher',
            managers=[
                ('objects', teacher.managers.TeacherManager()),
            ],
        ),
    ]