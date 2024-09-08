from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from app.models import Kitchen, Grill, Contact


# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):

        kitchens = Kitchen.objects.filter(show_on_site=True)
        grills = Grill.objects.filter(show_on_site=True)
        contact = Contact.objects.last()
        lst = []

        for i in kitchens:
            print(i.__dict__)
            lst.append(i.__dict__)

        for i in grills:
            print(i.__dict__)

        print("CONTACT: ", contact.__dict__)

        context = {"contact": contact}
        return render(request, "app/index.html", context)
