from django.urls import path, include

urlpatterns = [
  path('base/', include('app.urls.base')),
  path('categories/', include('app.urls.category')),
  path('suppliers/', include('app.urls.supplier')),
  path('products/', include('app.urls.product')),
  path('inventory/', include('app.urls.inventory')),
]
