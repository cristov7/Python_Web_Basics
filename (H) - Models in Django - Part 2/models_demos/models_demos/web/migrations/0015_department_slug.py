# Generated by Django 4.2.2 on 2023-06-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_alter_salary_options_department_created_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
