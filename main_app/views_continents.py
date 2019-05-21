from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Continent
from datetime import datetime

import logging

logger = logging.getLogger(__name__)

CONTINENTS_KEY_CACHE = "GEO_APP_CONTINENT_KEY"
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class ContinentsView(ListView):
    template_name = "main_app/continents.html"
    context_object_name = "continents_list"
    model = Continent

    def get_queryset(self):
        logger.info("[views_continents][ContinentsView][get_queryset][CACHE_TTL: " + str(CACHE_TTL) + "]")

        if CONTINENTS_KEY_CACHE in cache:
            logger.info("[views_continents][ContinentsView][get_queryset][retrieving continents from cache]")
            
            continents = cache.get(CONTINENTS_KEY_CACHE)
            
            return continents
        else:
            logger.info("[views_continents][ContinentsView][get_queryset][retrieving continents from db]")

            continents = Continent.objects.all()
            cache.set(CONTINENTS_KEY_CACHE, continents, timeout=CACHE_TTL)

            return continents


class ContinentCreateView(CreateView):
    model = Continent
    fields = ['name']
    success_url = "/continents"

    def get_success_url(self):
        logger.info("[views_continents][ContinentsView][get_success_url]")
        
        if CONTINENTS_KEY_CACHE in cache:
            logger.info("[views_continents][ContinentsView][get_success_url][CONTINENTS_KEY_CACHE exists in cache and will be deleted]")
            cache.delete(CONTINENTS_KEY_CACHE)

        return self.success_url

class ContinentUpdateView(UpdateView):
    model = Continent
    fields = ['name']
    success_url = "/continents"
    template_name = "main_app/continent_edit_form.html"

    def get_success_url(self):
        logger.info("[views_continents][ContinentUpdateView][get_success_url]")
        
        if CONTINENTS_KEY_CACHE in cache:
            logger.info("[views_continents][ContinentUpdateView][get_success_url][CONTINENTS_KEY_CACHE exists in cache and will be deleted]")
            cache.delete(CONTINENTS_KEY_CACHE)

        return self.success_url

class ContinentDeleteView(DeleteView):
    model = Continent
    success_url = "/continents"

    def get_success_url(self):
        logger.info("[views_continents][ContinentDeleteView][get_success_url]")
        
        if CONTINENTS_KEY_CACHE in cache:
            logger.info("[views_continents][ContinentDeleteView][get_success_url][CONTINENTS_KEY_CACHE exists in cache and will be deleted]")
            cache.delete(CONTINENTS_KEY_CACHE)

        return self.success_url
