from django.contrib import admin
from .models import *

#class and method that allows to create and customise models
class ProfileAdmin(admin.ModelAdmin):
    #Sort registers by date of creation
    date_hierarchy = 'created_at'
    #Shows chosen user attributes (columns)
    list_display = ('user', 'birth', 'role', 'addressesList')
    #Allows us to change empty registers to chose 'message'
    empty_value_display = '---'
    #Add link to others attributes listed by "list_display"
    list_display_links = ('user', 'role',)
    #Create a filter on screen (right side)
    list_filter = ('user__is_active',)
    #To determine which fields will be showned on create user form. 
    # ***Don't let not null fields out of this.***
    """ fields = (
    'user', ('role', ), 'image', 'birthday', 'addresses',) """
    #To exclude fields to be showned on create user form.
    exclude = ('favorites', 'specialties' 'created_at', 'updated_at',)
    #Fields set to be 'readonly' on create and edit user forms.
    readonly_fields = ('user',)
    #text field that allows user to search for the chosen fields (parameters).
    #don't work with integers (must use list_filter=('user__is__active', 'role'))
    search_fields = ('user__username',)
    #similar to "fields" but here its possible to group related fields
    fieldsets = (
        ('Usuário', {
            'fields': ('user', 'birthday', 'image')
        }),
        ('Função', {
            'fields': ('role',)
        }),
    )
    #method to custom birthday
    def birth(self, obj):
        if obj.birthday:
            return obj.birthday.strftime("%d/%m/%Y")
    birth.empty_value_display = '___/___/_____'

    #method to custam ManyToMany field
    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]

    #class responsable to hadle css and js files
    class Media:
        css = {
            "all": ("css/custom.css",)
        }
        js = ("js/custom.js",)


# Register your models here.
#Class "ProfileAdmin" passed as parameter of register method
admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Genre)
admin.site.register(Movie)

