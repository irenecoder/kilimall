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