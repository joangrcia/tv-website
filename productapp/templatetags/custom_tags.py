from django import template

register = template.Library()

@register.filter
def is_ebook(product):
    return product.product_type == 'book'
