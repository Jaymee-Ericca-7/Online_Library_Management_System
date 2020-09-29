# Generated by Django 3.0.4 on 2020-09-29 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library_system', '0010_auto_20200929_0557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='date_update',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='imprint',
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='borrower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='version',
            field=models.CharField(help_text='description or version of book copy (eq. "5th edition" )', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('Available', 'Available'), ('Reserved', 'Reserved')], default='Available', help_text='Book Availability', max_length=20),
        ),
    ]