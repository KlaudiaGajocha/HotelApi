from rest_framework import serializers
from hotel.models import Hotel, Attraction, Category, Rate

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class HotelFilterSerializer(serializers.Serializer):
    pk = serializers.IntegerField(
        required=False)
    name = serializers.CharField(
        required=False,
        max_length=10)
    rate_from = serializers.DecimalField(
        max_digits=1,
        decimal_places=0,
        required=False)
    rate_to = serializers.DecimalField(
        max_digits=1,
        decimal_places=0,
        required=False)
    
    
class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = "__all__"


class AttractionFilterSerializer(serializers.Serializer):
    pk = serializers.IntegerField(
         required=False)
    name = serializers.CharField(
        required=False,
        max_length=50)
    price_from = serializers.DecimalField(
        max_digits=100000,
        decimal_places=2,
        required=False)
    price_to = serializers.DecimalField(
        max_digits=100000,
        decimal_places=2,
        required=False)


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"


class RateFilterSerializer(serializers.Serializer):
    pk = serializers.IntegerField(
        required=False)
    value = serializers.DecimalField(
        max_digits=10,
        decimal_places=0,
        required=False)
    value_from = serializers.DecimalField(
        max_digits=10,
        decimal_places=0,
        required=False)
    value_to = serializers.DecimalField(
        max_digits=10,
        decimal_places=0,
        required=False)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryFilterSerializer(serializers.Serializer):
    pk = serializers.IntegerField(
         required=False)
    name = serializers.CharField(
        required=False,
        max_length=100)
