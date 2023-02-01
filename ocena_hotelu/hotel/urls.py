from django.urls.conf import path
from hotel.views import hotels, create, update, filter_hotels, delete_hotel, \
    attractions, create_attraction, update_attraction, filter_attraction, delete_attraction, \
    rates, create_rate, update_rate, filter_rate, delete_rate_hotel, \
    categories, filter_categories, createCategory, updateCategory, deleteCategory
from pip._vendor.requests.api import delete
from django.contrib import admin
from django.urls.conf import include


urlpatterns = [
    path("get_hotels/<int:pk>/", hotels),
    path("get_hotels", hotels),
    path("create", create),
    path("update", update),
    path("filter", filter_hotels,),
    path("delete_hotel", delete_hotel,),
    path("get_attractions/<int:pk>/", attractions),
    path("get_attractions", attractions),
    path("create_attraction", create_attraction),
    path("update_attraction", update_attraction),
    path("delete_attraction", delete_attraction),
    path("filter_attraction", filter_attraction,),
    path("get_rates/<int:pk>/", rates),
    path("get_rates", rates),
    path("create_rate", create_rate),
    path("update_rate", update_rate),
    path("delete_rate_hotel", delete_rate_hotel),
    path("filter_rate", filter_rate,),
    path("get_categories/<int:pk>/", categories),
    path("get_categories", categories),
    path("createCategory", createCategory),
    path("updateCategory", updateCategory),
    path("deleteCategory", deleteCategory),
    path("filter_categories", filter_categories,),

    
]



