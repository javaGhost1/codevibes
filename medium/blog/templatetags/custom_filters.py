# custom_filters.py
from django import template
from django.utils import formats
from django.utils.timezone import now
from datetime import timedelta

register = template.Library()

@register.filter
def relative_time(value):
    """
    Returns the relative time in a human-readable format.
    """
    time_difference = now() - value

    # Calculate years, months, days, and hours
    years = time_difference.days // 365
    months = (time_difference.days % 365) // 30
    days = (time_difference.days % 365) % 30
    hours = time_difference.seconds // 3600
    minutes = time_difference.seconds // 60

    if years > 0:
        return f"{years} year{'s' if years > 1 else ''} ago"
    elif months > 0:
        return formats.date_format(value, "F d")
        return f"{months} month{'s' if months > 1 else ''} ago"
    elif days > 0:
        return f"{days} day{'s' if days > 1 else ''} ago"
    elif hours > 0:
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif minutes > 0:
        return  f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    else:
        return "Just now"
