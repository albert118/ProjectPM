"""
Quick and easy, use the generic template views for Home & About page.
"""

from django.views import generic

class HomePage(generic.TemplateView):
    template_name = "home.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"