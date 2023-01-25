from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm
from kili.models import Product

@require_POST
def cart_add(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    cart= Cart(request)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],override_quantity=cd['override'])
    return redirect('cart:cart_detail')
