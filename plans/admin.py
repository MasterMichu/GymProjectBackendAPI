from django.contrib import admin
from .models import AvilableExcercises, Plans, Musclesgroup, Traninglog, PlanName

# Register your models here.
admin.site.register(AvilableExcercises)
admin.site.register(Plans)
admin.site.register(Musclesgroup)
admin.site.register(Traninglog)
admin.site.register(PlanName)