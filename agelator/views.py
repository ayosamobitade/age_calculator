from django.shortcuts import render

# Create your views here.
from django.http import request


def age_page(request):
    birthday = True
    days_lived = 1
    hours_lived = 2
    seconds_lived = 3
    calculated_birthday = 4
    sleep_days = 5

    return render(request, "static/age.html",
    {
        "days_lived":days_lived,
        "hours_lived":hours_lived,
        "seconds_lived":seconds_lived,
        "calculated_birthday":calculated_birthday,
        "sleep_days":sleep_days, 
        "birthday":birthday
    })