from django.shortcuts import render,redirect,get_object_or_404
from listings.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date')
    paginator = Paginator(listings,2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context= {"listings":paged_listings}
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {"listing":listing}
    return render(request,'listings/listing.html',context)
def search(request):

    return render(request,'listings/search.html')
