import stripe
import os

from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from dotenv import load_dotenv

from buy.models import Item

load_dotenv()

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

YOUR_DOMAIN = "http://127.0.0.1:8000"


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'


class ItemLandingPageView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.get(pk=1)
        context = super(ItemLandingPageView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            'STRIPE_PUBLIC_KEY': os.getenv('STRIPE_PUBLISHABLE_KEY')
        })
        return context


class CreateCheckoutSession(View):
    def post(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                            'description': item.description
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )

        return JsonResponse({
            'id': checkout_session.id
        })
