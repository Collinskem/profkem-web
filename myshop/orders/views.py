from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
#from . tasks import order_created
from cart.cart import Cart

@login_required(login_url="/accounts/login/")
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()

            #order_created.delay(order.id)
            #request.session['order_id']=order.id
            #return redirect(reverse('payment:process'))
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})
