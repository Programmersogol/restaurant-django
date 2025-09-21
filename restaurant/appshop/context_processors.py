from .models import Cart

def cart_item_count(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        session_id = request.session.session_key
        cart = Cart.objects.filter(session_id=session_id).first()

    if cart:
        return {'cart_item_count': sum(item.quantity for item in cart.cartitem_set.all())}
    return {'cart_item_count': 0}
