# -*- coding: utf-8 -*-

from django import template
from django.template.loader import render_to_string


register = template.Library()


@register.simple_tag
def cookielaw_banner(request):
    if request.COOKIES.get('cookielaw_accepted', False):
        return ''
    return render_to_string('cookielaw/banner.html', {})

