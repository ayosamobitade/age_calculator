from django.shortcuts import redirect, render

# Create your views here.
from django.http import request


def age_page(request):
    birthday_input = ""
    if request.method == 'POST':
        if request.POST.get('age_submit'):
            birthday_input = request.POST['birth_day']
            
            
        else:
            redirect('age_html')
            birthday_input = ""
    else:
        print("Error Occurred")

    
    return render(request, "static/age.html",
    {
     "birth_day" : birthday_input
    })