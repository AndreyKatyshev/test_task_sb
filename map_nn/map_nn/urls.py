from django.contrib import admin
from django.urls import path
from city import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nn/', views.nn)
]
