from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import AgencyForm
from .models import Agency


def agencies_search_view(request):
    query_dict = request.GET

    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    agency_obj = None

    if query is not None:
        agency_obj = Agency.objects.get(id=query)

    context = {"object": agency_obj}
    return render(request, "pages/agencies/search.html", context=context)


@login_required
def agencies_create_view(request):
    form = AgencyForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        agency_object = form.save()
        context["form"] = AgencyForm()
    return render(request, "pages/agencies/create.html", context=context)


def agencies_detail_view(request, id=None):
    agency_obj = None
    if id is not None:
        agency_obj = Agency.objects.get(id=id)
    context = {
        "object": agency_obj,
    }

    return render(request, "pages/agencies/detail.html", context=context)
