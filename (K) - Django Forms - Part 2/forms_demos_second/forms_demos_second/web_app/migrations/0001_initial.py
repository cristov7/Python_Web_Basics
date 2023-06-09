# Generated by Django 4.2.2 on 2023-06-23 21:38

from django.db import migrations, models
import forms_demos_second.web_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('done', models.BooleanField(default=False)),
                ('priority', models.IntegerField(validators=[forms_demos_second.web_app.validators.min_value_validator_func, forms_demos_second.web_app.validators.max_value_validator_func])),
            ],
        ),
    ]
