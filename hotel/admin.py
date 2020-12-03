from django.contrib import admin

from hotel.models import Room, HotelInfo, Blog


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'price', 'num_room')
    search_fields = ('room_type',)


class Hotel(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_name', 'post_date')


admin.site.register(Room, RoomAdmin)
admin.site.register(HotelInfo, Hotel)
admin.site.register(Blog, BlogAdmin)

