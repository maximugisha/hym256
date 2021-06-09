from django.contrib import admin
from .models import Language, Hymn, HymnNumber, HymnFile, Ad
# Register your models here.
admin.site.register(Language)
admin.site.register(Hymn)
admin.site.register(HymnNumber)
admin.site.register(HymnFile)
admin.site.register(Ad)
