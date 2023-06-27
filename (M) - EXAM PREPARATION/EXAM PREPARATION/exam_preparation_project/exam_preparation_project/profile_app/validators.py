from django.core.exceptions import ValidationError


def consist_only_of_letters_numbers_and_underscore_func(value: str):
    for char in value:
        if not (char.isalnum() or char == '_'):
            raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
