# Generated by Django 4.2.2 on 2023-06-11 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='desk',
            field=models.CharField(choices=[('first', 'desk 1'), ('last', 'desk 2')]),
        ),
    ]