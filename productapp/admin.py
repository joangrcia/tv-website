from django.contrib import admin
from .models import Product, Purchase, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_type', 'category', 'version', 'last_update', 'rating']
    list_filter = ['category', 'product_type', 'rating']
    search_fields = ['title', 'product_type', 'category__name']
    # Tambahkan field photo dan file sesuai dengan konfigurasi Anda

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'mt_name', 'token', 'purchase_date', 'is_confirmed')
    list_filter = ('purchase_date', 'is_confirmed')
    search_fields = ('user__username', 'product__title', 'mt_name')

    actions = ['confirm_payment']

    def confirm_payment(self, request, queryset):
        # Implementasi logika konfirmasi pembayaran di sini
        # Setelah konfirmasi berhasil, perbarui is_confirmed menjadi True

        for purchase in queryset:
            if not purchase.is_confirmed:
                # Lakukan konfirmasi pembayaran
                # Set purchase.is_confirmed = True
                purchase.is_confirmed = True
                purchase.save()

        self.message_user(request, f"{queryset.count()} pembelian telah dikonfirmasi.")

    confirm_payment.short_description = "Konfirmasi Pembayaran Terpilih"
