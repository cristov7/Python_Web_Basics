from django.core.exceptions import ValidationError
from datetime import date


def prevent_users_from_selecting_a_date_earlier_than_today_func(value) -> [ValidationError, None]:

    if value < date.today():
        raise ValidationError('The date cannot be in the past!')
