from django.urls import path
from django.views.generic import TemplateView

from .views_continents import ContinentsView
from .views_continents import ContinentCreateView
from .views_continents import ContinentUpdateView
from .views_continents import ContinentDeleteView

urlpatterns = [
    
    path('', TemplateView.as_view(template_name="main_app/index.html"), name='index'),

    path('continents/', ContinentsView.as_view(), name='continents'),
    path('continents/addContinent/', ContinentCreateView.as_view(), name='addContinent'),
    path('continents/editContinent/<int:pk>', ContinentUpdateView.as_view(), name='editContinent'),
    path('continents/deleteContinent/<int:pk>', ContinentDeleteView.as_view(), name='deleteContinent'),

]
