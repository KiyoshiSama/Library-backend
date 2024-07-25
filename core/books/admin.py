from django.contrib import admin
from .models import Author, Book, Publisher, Category

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'category', 'publish_date', 'is_available', 'created', 'updated')
    search_fields = ('title',)
    list_filter = ('publisher', 'category', 'is_available')
    filter_horizontal = ('authors',)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'created', 'updated')
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Category, CategoryAdmin)
