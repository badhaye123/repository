from django.urls import path 
from .import views

urlpatterns = [
    path('tv/',views.testView,name='tv'),
    path('add-order/',views.addOrderView,name='addorder'),
    path('show-orders/',views.showOrderView,name='showorders'),
    path('update-order/<int:id_from_fe>/',views.updateOrderView,name='updateorder'),
    path('delete-order/<int:id_from_fe>/',views.deleteOrderView,name='deleteorder')
]