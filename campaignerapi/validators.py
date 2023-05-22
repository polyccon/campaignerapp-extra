from datetime import (
    datetime,
    timedelta,
)

from rest_framework.exceptions import ValidationError


def date_is_present_or_future(value):
    today = datetime.utcnow().date()
    if isinstance(value, datetime):
        if value.date() < today:
            raise ValidationError("The date entered must be today or greater.")
    else:
        raise ValidationError(
            "The value entered isn't a valid type of date or datetime."
        )
