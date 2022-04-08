from django.core.exceptions import ValidationError

def vid_size (value):
    vidsize = value.size
    if vidsize > 20000000:
        raise ValidationError("maximum size is 20 mb")
    