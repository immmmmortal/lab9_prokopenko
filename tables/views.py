from django.shortcuts import render

from tables.models import Citizen, IncomeStatement


def show_citizen_table(request):  # Displays hotel table
    citizen_list = Citizen.objects.all()
    return render(request, 'show_citizen_table.html',
                  {'citizen_list': citizen_list})


def show_income_statement_table(request):  # Displays guest table
    income_statement_list = IncomeStatement.objects.all()
    return render(request, 'show_income_statement_table.html',
                  {'income_statement_list': income_statement_list})
