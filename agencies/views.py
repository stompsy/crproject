from django.shortcuts import render

from .models import Agency

# Create your views here.


def agencies_search_view(request):
    print(request.GET)
    query_dict = request.GET  # dictionary object
    # query = query_dict.get("q")  # q is the key, None is default value

    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    agency_obj = None
    if query is not None:
        agency_obj = Agency.objects.get(id=query)

    context = {"object": agency_obj}
    return render(request, "agencies/search.html", context=context)


def agencies_detail_view(request, id=None):
    agency_obj = None
    if id is not None:
        agency_obj = Agency.objects.get(id=id)
    context = {
        "object": agency_obj,
    }

    return render(request, "agencies/detail.html", context=context)
