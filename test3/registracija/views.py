# from django.shortcuts import render
# from django.http import HttpResponse
# from perziura.models import Klientas, Marke, Modelis


# def registracija(request):
#     if request.method=='POST':
#         user_name = request.POST.get('user_name')
#         user_last_name = request.POST.get('last_name')
#         user_date = request.POST.get('date')
#         user_email = request.POST.get('email')
#         user_marke = request.POST.get('marke')
#         user_modelis = request.POST.get('modelis')
#         user_metai = request.POST.get('metai')
#         new = Klientas(vardas = user_name, pavarde = user_last_name, gimimo_data = user_date, email = user_email)
#         new.save()
#         marke = Marke(automobilio_marke = user_marke)
#         modelis = Modelis(automobilio_modelis = user_modelis)
#         metai = Metai(automobilio_pagaminimo_metai = user_metai)
#         marke.save()
#         modelis.save()
#         metai.save()
#         modelis.metai.add(metai)
#         marke.modelis.add(modelis)
#         new.marke.add(marke)
    
#         new.save()
#     print(request.META['USER'])
# #    return HttpResponse("Hello, world. You're at the registracija page.")
#     return render(request, 'registracija.html')
