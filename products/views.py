import stripe
from django.conf import settings
from django.views.generic import TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        products = Item.objects.all()
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'items': products})
        return context


class ItemView(TemplateView):
    template_name = 'item.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        product = get_object_or_404(Item, pk=pk)
        context = super(ItemView, self).get_context_data(**kwargs)
        context.update({'product': product})
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']
        product = get_object_or_404(Item, pk=product_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000/'
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': product.price * 100,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"
