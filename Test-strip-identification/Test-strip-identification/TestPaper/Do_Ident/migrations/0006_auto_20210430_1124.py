# Generated by Django 3.1.2 on 2021-04-30 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Do_Ident', '0005_auto_20210430_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testpaper',
            name='result',
            field=models.CharField(default=None, max_length=64),
        ),
    ]
