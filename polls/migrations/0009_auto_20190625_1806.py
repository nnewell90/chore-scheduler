# Generated by Django 2.2.1 on 2019-06-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_hours_per_semester_funct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours_per_semester_funct',
            name='hours_per_semester_text',
            field=models.CharField(max_length=20000),
        ),
    ]
