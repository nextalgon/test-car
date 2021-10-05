from django.urls import path
from .views import CarDetialApi, CarsView, CliensView, ClientDetailApi, OrderView, \
    OrderDetailApi, ExOrderDetailApi, ExOrderView, car_bounty, order_exorder, client_bounty, find_time

urlpatterns = [
    path('car/<int:id>/', CarDetialApi.as_view()),
    path('car/', CarsView.as_view()),
    path('client/<int:id>/', ClientDetailApi.as_view()),
    path('client/', CliensView.as_view()),
    path('order/', OrderView.as_view()),
    path('order/<int:id>/', OrderDetailApi.as_view()),
    path('exorder/', ExOrderView.as_view()),
    path('exorder/<int:id>/', ExOrderDetailApi.as_view()),
    path('carbounty/', car_bounty),
    path('orderex/', order_exorder),
    path('clientbounty/', client_bounty),
    path('time/', find_time)
]
