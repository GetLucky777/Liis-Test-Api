import re

from django.core.exceptions import ValidationError


class NumberAndLetterValidator:

    def validate(self, password, user=None):
        if not re.search(r'\d.*[a-zA-Z]|[a-zA-Z].*\d', password):
            raise ValidationError(
                'Password must have at least one letter and one number!'
            )

    def get_help_text(self):
        return 'Your password must contain at least one letter and one number!'
