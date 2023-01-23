from decimal import Decimal
from django.conf import settings
from kili.models import Product

class Cart(object):
    def __init__(self,request):
        #initialize the session as a request
        self.session = request.session
        # try and get the cart in session
        cart= self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # save empty cart in the session
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart = cart

    def add(self,product,quantity=1,override_quantity=False):
        #stringify product id for JSON so that it is serialized
        product_id = str(product.id)
        #add item in cart,with product id as key and a dictionary containing quantity and price as value
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':0,'price':str(product.price)}
        #update while checking if theres overriding
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self,product):
        """remove a product from the cart"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        # iterate through items in the cart and get the objects from the database
        product_ids=self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        # add the product objects to the cart
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price']*item['quantity']
            yield item




