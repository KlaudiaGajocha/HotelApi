from django.contrib import admin
from hotel.models import Attraction, Category, Rate, Hotel
# from myproject.admin_site import custom_admin_site




@admin.register(Attraction, 
                    Category, 
                    Rate, 
                    Hotel,
                    #site=custom_admin_site
                    )

class PersonAdmin(admin.ModelAdmin):
    pass