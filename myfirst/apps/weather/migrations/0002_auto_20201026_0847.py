# Generated by Django 3.1.2 on 2020-10-26 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='temperature',
            field=models.IntegerField(),
        ),
    ]