# -*- coding: utf-8 -*-

from django import template
from django.template.loader import render_to_string


register = template.Library()


@register.simple_tag(takes_context=True)
def cookielaw_banner(context):
    if context['request'].COOKIES.get('cookielaw_accepted', False):
        return ''
    return render_to_string('cookielaw/banner.html', context)
