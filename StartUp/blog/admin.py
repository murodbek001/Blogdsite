from django.contrib import admin
from .models import Category,Post,Tag,Comment
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    fields = ('title', 'slug')
    prepopulated_fields = {"slug": ('title',)}

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')
    fields = ('title', 'slug', 'image','description', 'author', 'category','tag',)
    prepopulated_fields = {"slug":( 'title', )}
    list_filter = ('created', 'updated', 'category', 'author')
    search_fields = ('title', 'slug', 'description')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
