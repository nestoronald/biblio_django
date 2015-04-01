from django.contrib import admin

# Register your models here.
from models import *

# Register your models here.
admin.site.register(ItemType)
admin.site.register(Language)
admin.site.register(Item)
admin.site.register(Author)
admin.site.register(AuthorType)
admin.site.register(ItemAuthor)
admin.site.register(ItemDetails)
admin.site.register(ItemTheme)



