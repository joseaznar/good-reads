from django.contrib import admin
from .models import Book, Coments

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    pass


class ComentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Coments, ComentsAdmin)
admin.site.register(Book, BookAdmin)
