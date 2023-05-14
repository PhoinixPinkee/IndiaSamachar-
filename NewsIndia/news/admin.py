from django.contrib import admin
from  .models import contactus,news

from  .models import city,category,slider,videos,bnews


class contactusAdmin(admin.ModelAdmin):
    list_display = ("Name","Mobile","Email","Message");
class cityAdmin(admin.ModelAdmin):
    list_display = ('id','city' , 'cpic');
# Register your models here.
admin.site.register(contactus,contactusAdmin)
admin.site.register(city,cityAdmin)
class categoryAdmin(admin.ModelAdmin):
    list_display =("id","cname")
admin.site.register(category, categoryAdmin)
class newsAdmin(admin.ModelAdmin):
    list_display =('id','headline','ndes','city','newspic','category','cdate')
admin.site.register(news,newsAdmin)
class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','shead','ssubject','sdes','spic');
admin.site.register(slider,sliderAdmin)

class videosAdmin(admin.ModelAdmin):
    list_display = ('id','vhead','vdes','vpic','vlink');
admin.site.register(videos,videosAdmin)
class bnewsAdmin(admin.ModelAdmin):
    list_display = ('id','bhead','bdate','bpic','bdes');
admin.site.register(bnews,bnewsAdmin)