from django.core.exceptions import ValidationError


def contain_only_letter_validator(value: str):
    for letter in value:
        if not letter.isalpha():
            raise ValidationError('Fruit name should contain only letters!')
