from django.contrib import admin
from django.urls import path
from main.views import (
    CreateCheckoutSessionView,
    IndexView,
    ItemView,
    SuccessView,
    CancelView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("buy/<int:pk>/", CreateCheckoutSessionView.as_view(),
         name="create-checkout-session"),
    path("", IndexView.as_view(), name="index"),
    path('item/<int:pk>', ItemView.as_view(), name='item'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]
