from django.shortcuts import render

from tables.models import Hotel, Guest


def show_hotel_table(request):  # Displays hotel table
    hotel_list = Hotel.objects.all()
    return render(request, 'show_hotel_table.html',
                  {'hotel_list': hotel_list})


def show_guest_table(request):  # Displays guest table
    guest_list = Guest.objects.all()
    return render(request, 'show_guest_table.html',
                  {'guest_list': guest_list})
