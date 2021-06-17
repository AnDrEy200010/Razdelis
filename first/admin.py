from django.contrib import admin
from first.models import ProfilePhysPerson, Chapter, Category, ImagesItem, Item, Reservation

admin.site.register(ProfilePhysPerson)
admin.site.register(Chapter)
admin.site.register(Category)
admin.site.register(ImagesItem)
admin.site.register(Item)
admin.site.register(Reservation)