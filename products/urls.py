from django.urls import path
from .views import CreateCheckoutSessionView, ItemView, SuccessView, CancelView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('item/<int:pk>', ItemView.as_view(), name='item'),
    path('buy/<int:pk>', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('success', SuccessView.as_view(), name='success'),
    path('cancel', CancelView.as_view(), name='cancel')
]
