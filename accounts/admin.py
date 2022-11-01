from django.contrib import admin
from .models import Person, TimeTable, Subject

class PersonAdmin(admin.ModelAdmin):
    pass

class TimeTableAdmin(admin.ModelAdmin):
    pass
    
class SubjectAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Person, PersonAdmin)
admin.site.register(TimeTable, TimeTableAdmin)
admin.site.register(Subject, SubjectAdmin)