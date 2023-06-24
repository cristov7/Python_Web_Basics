from django.core.exceptions import ValidationError


# Custom function validator:
def min_value_validator_func(value: int):
    if value < 1:
        raise ValidationError(f'Priority must be GREATER OR EQUAL to 1 - NOT {value}!')


# Custom function validator:
def max_value_validator_func(value: int):
    if value > 10:
        raise ValidationError(f'Priority must be LOWER OR EQUAL to 10 - NOT {value}!')


# Custom class validator:
class ValueInRangeValidator:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value: int):
        if (value < self.min_value) or (value > self.max_value):
            raise ValidationError(f'Priority must be BETWEEN {self.min_value} AND {self.max_value} - NOT {value}!')
