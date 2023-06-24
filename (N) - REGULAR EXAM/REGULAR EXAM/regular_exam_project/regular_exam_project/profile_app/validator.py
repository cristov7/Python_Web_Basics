from django.core.exceptions import ValidationError


def start_with_a_letter_validator(value: str):
    if not value[0].isalpha():
        raise ValidationError('Your name must start with a letter!')
