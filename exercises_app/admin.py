from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Exercises)
admin.site.register(Answer)
admin.site.register(Sections)
admin.site.register(Subsections)
