# Generated by Django 3.1.2 on 2021-04-30 03:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Do_Ident', '0004_auto_20210430_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='testpaper',
            name='title',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='testpaper',
            name='result',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='testpaper',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
