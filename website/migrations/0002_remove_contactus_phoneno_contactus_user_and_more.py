# Generated by Django 4.2.4 on 2023-08-28 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='phoneno',
        ),
        migrations.AddField(
            model_name='contactus',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contactus',
            name='phoneNo',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
