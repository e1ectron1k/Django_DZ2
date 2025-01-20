from django.urls import path
from calculator.views import recipe_view

urlpatterns = [
    path('<str:recipe_name>/', recipe_view, name='recipe_view'),
]