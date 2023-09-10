# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# # request handler


# # Pull data from db
# # Transform
# # Send email
# def say_hello(request):
#     return render(request, 'hello.html',{'name': 'Brittani' })
    ##return HttpResponse('Hello World')


from rest_framework import generics
from django.http import HttpResponse
from .models import Item, Location
from .serializers import ItemSerializer, LocationSerializer

def say_hello(request):
    return render(request, 'hello.html',{'name': 'Brittani' })

#C for create
class ItemList(generics.ListCreateAPIView):
    serializer_class =ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(itemLocation=location)
        return queryset    
#R for retrieve U for Update D for Destroy
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):        
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer    
    queryset = Location.objects.all()

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer    
    queryset = Location.objects.all()    