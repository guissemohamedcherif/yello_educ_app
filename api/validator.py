import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length
        self.regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'  # Example regex

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _(f"Password must be at least {self.min_length} characters long."),
                code='password_too_short',
            )
        
        if not re.match(self.regex, password):
            raise ValidationError(
                _("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character."),
                code='password_invalid',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
        )