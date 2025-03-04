from django.contrib import admin
from.models import Activity
# Register your models here.
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title','date','created_at')#show fields in the admin list
    search_fields = ('title','description')#enable search
    list_filter = ('date',)#add filtering by date