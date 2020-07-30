from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at',)
    list_display = ('name', 'create_at')
    search_fields = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'update_at')
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    list_display = ('title', 'user', 'public', 'created_at')
    list_filter = ('public', 'user__username', 'categories__name')

    def save_model(sekf, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()


# Register your models here.
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
