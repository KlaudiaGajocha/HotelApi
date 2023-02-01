from django.shortcuts import render
from django.http.response import JsonResponse
from hotel.models import Attraction, Category, Rate, Hotel 
from django.views.decorators.csrf import csrf_exempt
from hotel.serializers import HotelSerializer, HotelFilterSerializer, AttractionSerializer, \
    AttractionFilterSerializer, RateSerializer, RateFilterSerializer, CategorySerializer, CategoryFilterSerializer
from rest_framework.parsers import JSONParser
from rest_framework import  viewsets
from rest_framework.generics import  get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions



def hotels (request, pk=0):
    result = {"hotels": []}
    if pk:
        hotels = Hotel.objects.filter(id=pk).order_by("name")
    else:
        hotels = Hotel.objects.all().order_by("-name")
    for hotel in hotels:
        result["hotels"].append({"name": hotel.name,
                                "owner": hotel.owner,
                                "localization": hotel.localization,
                                "description": hotel.description,
                                "attractions": hotel.attractions,
                                "category": hotel.category})
        

    return JsonResponse(result)

@csrf_exempt
def filter_hotels(request):
    data = JSONParser().parse(request)
    serializer = HotelFilterSerializer(data=data)
    if serializer.is_valid():
        if serializer.data.get("pk"):
            hotels = Hotel.objects.filter(id=serializer.data.get("pk")).order_by("name")
        elif serializer.data.get("name"):
            hotels = Hotel.objects.filter(name=serializer.data.get("name")).order_by("name")
        elif serializer.data.get("rate_from") or serializer.data.get("rate_to"):
            hotels = Hotel.objects.filter()
            if serializer.data.get("rate_from"):
                hotels = hotels.filter(price__gte=serializer.data.get("rate_from"))
            if serializer.data.get("rate_to"):
                hotels = hotels.filter(price__lte=serializer.data.get("rate_to"))
            hotels = hotels.order_by("name")
        else:
            hotels = Hotel.objects.all().order_by("-name")
        serializer_out = HotelSerializer(hotels, many=True)
        return JsonResponse(serializer_out.data, safe=False)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def create(request):
    data = JSONParser().parse(request)
    serializer = HotelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def update(request):
    data = JSONParser().parse(request)
    try:
        hotel = Hotel.objects.get(pk=data["id"])
    except Hotel.DoesNotExist:
        return JsonResponse({}, status=404)
    serializer = HotelSerializer(hotel, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def delete_hotel(request):
    data = JSONParser().parse(request)
    try:
        hotel = Hotel.objects.get(pk=data["id"])
    except Hotel.DoesNotExist:
        return JsonResponse({}, status=404)
    hotel.delete()
    return JsonResponse({}, status=204)



class HotelViewSet(viewsets.ModelViewSet):
    serializer_class = HotelSerializer 
    queryset = Hotel.objects.all()
    

    def get_permissions(self):
        permission_classes = []
        if self.action not in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
            
        return [permission()for permission in permission_classes]
    
    
    
# Attraction

def attractions(request, pk=0):
    result = {"attractions": []}
    if pk:
        attractions = Attraction.objects.filter(name=pk).order_by("name")
    else:
        attractions = Attraction.objects.all().order_by("-name")
    for attraction in attractions:
        result["attractions"].append({"name": attraction.name,
                                      "price": attraction.price,
                                      "description": attraction.description})
    return JsonResponse(result)


@csrf_exempt
def filter_attraction(request):
    data = JSONParser().parse(request)
    serializer = AttractionFilterSerializer(data=data)
    if serializer.is_valid():
        if serializer.data.get("name"):
            attractions = Attraction.objects.filter(name=serializer.data.get("name")).order_by("name")
        elif serializer.data.get("price_from") or serializer.data.get("price_to"):
            attractions = Attraction.objects.filter()
            if serializer.data.get("price_from"):
                attractions = attractions.filter(price__gte=serializer.data.get("price_from"))
            if serializer.data.get("price_to"):
                attractions = attractions.filter(price__lte=serializer.data.get("price_to"))
            attractions = attractions.order_by("name")
        else:
            attractions = Attraction.objects.all().order_by("-name")
        serializer_out = AttractionSerializer(attractions, many=True)
        return JsonResponse(serializer_out.data, safe=False)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def create_attraction(request):
    data = JSONParser().parse(request)
    serializer = AttractionSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def update_attraction(request):
    data = JSONParser().parse(request)
    try:
        attraction = Attraction.objects.get(name=data["name"])
    except Attraction.DoesNotExist:
        return JsonResponse({}, status=404)
    serializer = AttractionSerializer(attraction, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def delete_attraction(request):
    data = JSONParser().parse(request)
    try:
        attraction = Attraction.objects.get(name=data["name"])
    except Attraction.DoesNotExist:
        return JsonResponse({}, status=404)
    attraction.delete()
    return JsonResponse({}, status=204)


class AttractionViewSet(viewsets.ModelViewSet):
    serializer_class = AttractionSerializer
    queryset = Attraction.objects.all()
    
    def get_permissions(self):
        permission_classes = []
        if self.action not in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]

# Rate
def rates(request, pk=0):
    result = {"rates": []}
    if pk:
        rates = Rate.objects.filter(value=pk).order_by("value")
    else:
        rates = Rate.objects.all().order_by("-value")
    for rate in rates:
        result["rates"].append({"value": rate.value,
                                 "user": rate.user,
                                 "description": rate.description,
                                 "hotel": rate.hotel})
    return JsonResponse(result)


@csrf_exempt
def filter_rate(request):
    data = JSONParser().parse(request)
    serializer = RateFilterSerializer(data=data)
    if serializer.is_valid():
        if serializer.data.get("hotel"):
            rates = Rate.objects.filter(hotel=serializer.data.get("hotel")).order_by("hotel")
        elif serializer.data.get("user"):
            rates = Rate.objects.filter(user=serializer.data.get("user")).order_by("user")
        elif serializer.data.get("value_from") or serializer.data.get("value_to"):
            rates = Rate.objects.filter()
            if serializer.data.get("value_from"):
                rates = rates.filter(value__gte=serializer.data.get("value_from"))
            if serializer.data.get("value_to"):
                rates = rates.filter(value__lte=serializer.data.get("value_to"))
            rates = rates.order_by("value")
        else:
            rates = Rate.objects.all().order_by("-value")
        serializer_out = RateSerializer(rates, many=True)
        return JsonResponse(serializer_out.data, safe=False)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def create_rate(request):
    data = JSONParser().parse(request)
    serializer = RateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def update_rate(request):
    data = JSONParser().parse(request)
    try:
        rate = Rate.objects.get(value=data["value"])
    except Rate.DoesNotExist:
        return JsonResponse({}, status=404)
    serializer = RateSerializer(rate, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def delete_rate_hotel(request):
    data = JSONParser().parse(request)
    try:
        rate = Rate.objects.get(hotel=data["hotel"])
    except Rate.DoesNotExist:
        return JsonResponse({}, status=404)
    rate.delete()
    return JsonResponse({}, status=204)


class RateViewSet(viewsets.ModelViewSet):
    serializer_class = RateSerializer
    queryset = Rate.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action not in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

# Category

def categories(request, pk=0):
    result = {"categories": []}
    if pk:
        categories = Category.objects.filter(cathegory_name=pk).order_by("cathegory_name")
    else:
        categories = Category.objects.all().order_by("-cathegory_name")
    for category in categories:
        result["categories"].append({"category_name": category.cathegory_name})
    return JsonResponse(result)


@csrf_exempt
def filter_categories(request):
    data = JSONParser().parse(request)
    serializer = CategoryFilterSerializer(data=data)
    if serializer.is_valid():
        if serializer.data.get("cathegory_name"):
            categories = Category.objects.filter(cathegory_name=serializer.data.get("cathegory_name")).order_by("cathegory_name")
        else:
            categories = Category.objects.all().order_by("-cathegory_name")
        serializer_out = CategorySerializer(categories, many=True)
        return JsonResponse(serializer_out.data, safe=False)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def createCategory(request):
    data = JSONParser().parse(request)
    serializer = CategorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def updateCategory(request):
    data = JSONParser().parse(request)
    try:
        category = Category.objects.get(cathegory_name=data["cathegory_name"])
    except Category.DoesNotExist:
        return JsonResponse({}, status=404)
    serializer = CategorySerializer(category, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def deleteCategory(request):
    data = JSONParser().parse(request)
    try:
        category = Category.objects.get(cathegory_name=data["cathegory_name"])
    except Hotel.DoesNotExist:
        return JsonResponse({}, status=404)
    category.delete()
    return JsonResponse({}, status=204)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action not in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]

    
    