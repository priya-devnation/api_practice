# Django modules
from django.core.validators import RegexValidator

# Phone number validator
phone_validator = RegexValidator(regex=r'^\+?\d{10,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")