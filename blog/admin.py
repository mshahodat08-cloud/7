
from django.contrib import admin
from .models import Post, Izoh   # 🔥 Izohni ham qo‘shamiz

class PostAdmin(admin.ModelAdmin):
    list_display = ('sarlavha', 'muallif', 'yaratilgan_sana', 'nashr_etilgan')
    list_filter = ('nashr_etilgan', 'yaratilgan_sana')
    search_fields = ('sarlavha', 'matn')
    date_hierarchy = 'yaratilgan_sana'

admin.site.register(Post, PostAdmin)

class IzohInline(admin.TabularInline):
    model = Izoh
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [IzohInline]

admin.site.register(Izoh)

from .models import Post, Kategoriya

admin.site.register(Kategoriya)
