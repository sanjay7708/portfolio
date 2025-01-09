from django.db import models
from django.core.exceptions import ValidationError
import re

# Custom validator for phone numbers
def validate_phone(value):
    if not re.match(r'^\d{10}$', value):
        raise ValidationError("Phone number must be exactly 10 digits.")

class ContactModel(models.Model):
    name = models.CharField(max_length=100)  # Fixed the field definition
    email = models.EmailField()
    phone = models.CharField(
        max_length=10,
        validators=[validate_phone],
        help_text="Enter your 10-digit phone number without the country code."
    )

    def formatted_phone(self):
        # Return the phone number with the default country code
        return f"+91{self.phone}"
