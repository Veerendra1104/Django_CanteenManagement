from django.contrib import admin
from.models import Register_names, Registers, Item


# Register your models here.
admin.site.register(Register_names)

@admin.register(Registers)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    ordering = ('name',)
    search_fields = ('name',)
      

admin.site.register(Item)