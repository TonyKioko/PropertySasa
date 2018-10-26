from django.shortcuts import render,redirect,get_object_or_404
from listings.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import *

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date')
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context= {"listings":paged_listings}
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {"listing":listing,}
    return render(request,'listings/listing.html',context)
def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__icontains=city)
    if 'county' in request.GET:
        county = request.GET['county']
        if county:
            queryset_list=queryset_list.filter(county__icontains=county)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list=queryset_list.filter(price__lte=price)
    context = {"price_choices":price_choices,"bedroom_choices":bedroom_choices,"county_choices":county_choices,"listings":queryset_list,"values":request.GET}
    return render(request,'listings/search.html',context)
