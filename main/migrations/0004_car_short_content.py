# Generated by Django 2.2.7 on 2019-12-02 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_car_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='short_content',
            field=models.TextField(default=''),
        ),
    ]