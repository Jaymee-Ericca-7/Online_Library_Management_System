# Generated by Django 3.0.4 on 2020-09-29 17:55

from django.db import migrations, models
import library_system.models


class Migration(migrations.Migration):

    dependencies = [
        ('library_system', '0012_auto_20200929_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='due_back',
            field=models.DateField(default=library_system.models.get_deadline, null=True),
        ),
    ]