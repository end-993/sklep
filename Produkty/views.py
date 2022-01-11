from django.shortcuts import render
from django.http import HttpResponse
from .models import produkty,producent,kategoria


# Create your views here.
def index(request):
   # wszystkie = produkty.objects.all()
   # jeden = produkty.objects.get(pk=2)
   # nazwa_kat = kategoria.objects.all()
   # null = produkty.objects.filter(kategoria__isnull=False)
    #zawiera = produkty.objects.filter(opis__icortains='dysk')
    kategorie = kategoria.objects.all()
    dane = {'kategorie' : kategorie}
    return render(request,'szablon.html',dane)

def kategoria1(request,id):
    kategoria_user = kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user.nazwa)

def produkt1(request,id):
    produkt_user = produkty.objects.get(pk=id)
    return HttpResponse(produkt_user.nazwa)