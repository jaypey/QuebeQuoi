# Generated by Django 2.2.3 on 2019-08-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qqapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qq',
            name='qq_pic',
            field=models.CharField(max_length=800, null=True),
        ),
    ]
