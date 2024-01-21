"""
To render HTML web pages
"""

from django.http import HttpResponse
from django.template.loader import render_to_string
from agencies.models import Agency


def home_view(request, *args, **kwargs):
    agency_obj = Agency.objects.get(id=1)
    agency_queryset = Agency.objects.all()

    context = {
        "object_list": agency_queryset,
        "id": agency_obj.id,
        "agency_name": agency_obj.agency_name,
        "agency_description": agency_obj.agency_description,
        "agency_url": agency_obj.agency_url,
    }

    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_STRING)
