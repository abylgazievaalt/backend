# Generated by Django 3.0.7 on 2020-06-09 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200609_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]