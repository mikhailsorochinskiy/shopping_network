from django.contrib import admin, messages
from django.shortcuts import reverse
from django.utils.html import format_html
from .models import NetworkNode, Product

def clear_debt(modeladmin, request, queryset):
    """
    Admin action для обнуления задолженности у выбранных объектов.
    """
    updated_count = queryset.update(debt=0)
    modeladmin.message_user(
        request,
        f"Задолженность успешно обнулена для {updated_count} объектов.",
        messages.SUCCESS
    )

clear_debt.short_description = "Обнулить задолженность у выбранных звеньев"

@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supplier_link', 'debt', 'country', 'city', 'level_display')
    list_filter = ['city']
    actions = [clear_debt]
    readonly_fields = ['supplier_link']

    def supplier_link(self, obj):
        """
        Создает кликабельную ссылку на страницу изменения поставщика.
        """
        if obj.supplier:
            url = reverse('admin:shop_net_networknode_change', args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return "—"

    supplier_link.short_description = "Поставщик"

    def level_display(self, obj):
        return obj.level_display  # Предполагая, что у модели есть этот метод

    level_display.short_description = "Уровень"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'release_date']
