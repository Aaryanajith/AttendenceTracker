# Generated by Django 4.2.5 on 2023-09-24 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_attendance_attandence_log_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
