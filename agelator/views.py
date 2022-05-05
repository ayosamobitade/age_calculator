from django.shortcuts import redirect, render
from . import age_calculate

# Create your views here.
from django.http import request


def age_page(request):
    birthday_input = ""
    time_input = 0
    day_spent = ""
    hour_spent=""
    second_spent=""
    sleep_day = ""
    sleep_hour = ""
    if request.method == 'POST':
        if request.POST.get('age_submit'):
            birthday_input = request.POST['birth_day']
            time_input = request.POST['birth_time']
            agilator = age_calculate.birthday_calculator(birthday_input, time_input)
            day_spent = agilator.num_day_lived()
            hour_spent = agilator.num_hours_lived()
            second_spent=agilator.num_seconds_lived()
            sleep_day = agilator.num_sleep_day()
            sleep_hour = agilator.num_sleep_hour()

                        
        else:
            redirect('age_html')
            birthday_input = ""
            time_input = ""
            day_spent = ""
            hour_spent=""
            second_spent=""
            sleep_day = ""
            sleep_hour = ""
    else:
        print("Error Occurred")
  
    return render(request, "static/age.html",
    {
     "birth_day" : birthday_input,
     "birth_time": time_input,
     "day_spent" : f'{day_spent:,}',
     "hour_spent":hour_spent,
     "second_spent":second_spent,
     "sleep_day" : sleep_day,
     "sleep_hour": sleep_hour
    })