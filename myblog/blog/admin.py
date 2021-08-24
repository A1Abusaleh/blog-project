from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'name', 'author', 'creation_date',)
    list_filter = ('title','author')
    search_fields = ['title', 'content']
    
   # prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Books, BooksAdmin)
