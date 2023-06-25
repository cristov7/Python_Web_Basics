# Generated by Django 4.2.2 on 2023-06-24 21:35

import django.core.validators
from django.db import migrations, models
import regular_exam_project.fruit_app.validator


class Migration(migrations.Migration):

    dependencies = [
        ('fruit_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruitmodel',
            name='name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), regular_exam_project.fruit_app.validator.contain_only_letter_validator]),
        ),
    ]