from django.urls import path

from .views import CreateCheckoutSession

urlpatterns = [
    path('create-checkout-session/<pk>/', CreateCheckoutSession.as_view(), name='create-checkout-session')
]
