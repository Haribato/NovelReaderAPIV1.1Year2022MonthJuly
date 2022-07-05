from django.contrib import admin

from .models import *


admin.site.register(Status)
admin.site.register(Language)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Source)
admin.site.register(Books)
admin.site.register(Chapters)


