from django.shortcuts import render

from .models import Agency

# Create your views here.


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
    return render(request, "agencies/search.html", context=context)


def agencies_create_view(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("agency_name")
        url = request.POST.get("agency_url")
        description = request.POST.get("agency_description")
        agency_object = Agency.objects.create(
            agency_name=name, agency_url=url, agency_description=description
        )
        context["object"] = agency_object
        context["created"] = True
    return render(request, "agencies/create.html", context=context)


def agencies_detail_view(request, id=None):
    agency_obj = None
    if id is not None:
        agency_obj = Agency.objects.get(id=id)
    context = {
        "object": agency_obj,
    }

    return render(request, "agencies/detail.html", context=context)
