from django.contrib import admin
from .models import Office, Equipment, Person


class PropertyAcct(admin.ModelAdmin):
    list_display = ('user', 'qty','unit','desc1', 'desc2', 'date_acquired', 'prop_num','unit_cost','total_cost')
    list_filter =('user', 'date_acquired')
#    list_editable = ('qty','unit','desc1', 'desc2', 'date_acquired', 'prop_num','unit_cost','total_cost')
    search_fields =('user',)
    list_per_page = 10

admin.site.register(Office)
admin.site.register(Equipment,PropertyAcct)
admin.site.register(Person)
