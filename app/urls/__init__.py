from django.urls import path, include

urlpatterns = [
  path('base/', include('app.urls.base')),
  path('categories/', include('app.urls.category')),
  path('products/', include('app.urls.product')),
  path('inventory/', include('app.urls.inventory')),
  path('sales/', include('app.urls.sale')),
]
