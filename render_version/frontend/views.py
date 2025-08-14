from django.shortcuts import render, get_object_or_404
from properties.models import Property, PropertyType
from contacts.models import Contact


def home_view(request):
    featured_properties = Property.objects.filter(featured=True, status="available")[:6]
    property_types = PropertyType.objects.all()

    context = {
        "featured_properties": featured_properties,
        "property_types": property_types,
    }
    return render(request, "frontend/home.html", context)


def property_list_view(request):
    properties = Property.objects.filter(status="available")
    property_types = PropertyType.objects.all()

    # Filter by property type
    property_type = request.GET.get("type")
    if property_type:
        properties = properties.filter(property_type__slug=property_type)

    # Filter by location
    city = request.GET.get("city")
    if city:
        properties = properties.filter(city__icontains=city)

    context = {
        "properties": properties,
        "property_types": property_types,
        "current_type": property_type,
        "current_city": city,
    }
    return render(request, "frontend/property_list.html", context)


def property_detail_view(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    related_properties = Property.objects.filter(
        property_type=property_obj.property_type, status="available"
    ).exclude(pk=pk)[:4]

    context = {
        "property": property_obj,
        "related_properties": related_properties,
    }
    return render(request, "frontend/property_detail.html", context)


def contact_view(request):
    return render(request, "frontend/contact.html")
