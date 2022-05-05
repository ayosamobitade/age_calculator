from django.shortcuts import redirect, render
from . import age_calculate

# Create your views here.
from django.http import request


def age_page(request):
    birthday_input = ""
    time_input = ""
    day_spent = ""
    if request.method == 'POST':
        if request.POST.get('age_submit'):
            birthday_input = request.POST['birth_day']
            time_input = request.POST['birth_time']
            agilator = age_calculate.birthday_calculator(birthday_input, time_input)
            day_spent = agilator.num_day_lived()

                        
        else:
            redirect('age_html')
            birthday_input = ""
            time_input = ""
    else:
        print("Error Occurred")
  
    return render(request, "static/age.html",
    {
     "birth_day" : birthday_input,
     "birth_time": time_input,
     "day_spent" : day_spent
    })