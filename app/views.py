from django.shortcuts import render
from django.views import View

from app.models import Kitchen, Grill, Contact


class IndexView(View):
    def get(self, request, *args, **kwargs):

        context = {
            "kitchens": Kitchen.objects.filter(show_on_site=True),
            "grills": Grill.objects.filter(show_on_site=True),
            "contact": Contact.objects.last()
        }
        return render(request, "app/index.html", context)
