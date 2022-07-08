from django.contrib import admin
from django.urls import path
from . import views

# ```
# /brands # a list of all the car brands
# /brands/new # form for a new car brand
# /brands/<:id> # see a specific car brand
# /brands/<:id>/edit # edit page for a specific car brand

# /brands/<:brand_id>/cars # a list of cars for a specific car brand
# /brands/<:brand_id>/cars/new # form for a new car under a specific car brand
# /brands/<:brand_id>/cars/<:car_id> # see a specific car for a specific car brand
# /brands/<:brand_id>/cars/<:car_id>/edit # edit page for a specific car under a specific car brand
# ```

urlpatterns = [
    path('', views.index),
    path('brands/', views.brands),
    path('brands/new/', views.brand_new_form),
    path('brands/<int:id>/', views.brand_show),
    path('brands/<int:id>/edit/', views.brand_edit),
    path('brands/<int:brand_id>/cars/', views.brand_list_cars),
    path('brands/<int:brand_id>/cars/new/', views.brand_new_car_form),
    path('brands/<int:brand_id>/cars/<int:car_id>/', views.brand_specific_car),
    path('brands/<int:brand_id>/cars/<int:car_id>/edit/', views.brand_specific_car_edit),
]