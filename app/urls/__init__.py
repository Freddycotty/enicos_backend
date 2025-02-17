from django.urls import path, include

urlpatterns = [
  path('base/', include('app.urls.base')),
]
