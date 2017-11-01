import hashlib
import urllib.parse
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=40):
    default = "http://127.0.0.1:8000/media/img/acg.png"
    # default = "{% static 'img/logo.jpg'%}"
    return "https://www.gravatar.com/avatar/%s?%s" % (
    hashlib.md5(email.lower().encode(encoding='utf-8')).hexdigest(), urllib.parse.urlencode({'d': default, 's': str(size)}))


# return an image tag with the gravatar
# TEMPLATE USE:  {{ email|gravatar:150 }}
@register.filter
def gravatar(email, size=40):
    url = gravatar_url(email, size)
    return mark_safe('<img src="%s" width="%d" height="%d">' % (url, size, size))