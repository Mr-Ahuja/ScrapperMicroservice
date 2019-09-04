
from django.urls import path

from .views import StockURLView,StockInfoNSEView

app_name = "StockURL"

urlpatterns = [
    path('stockurl/', StockURLView.as_view()),
    path('stockinfo/<str:name>', StockInfoNSEView.as_view()),
]