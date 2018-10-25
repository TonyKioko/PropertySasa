from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.

def index(request):

    listings = Listing.objects.all()[:3]
    context ={"listings":listings}
    return render(request,'pages/index.html',context)

def about(request):

    return render(request,'pages/about.html')
