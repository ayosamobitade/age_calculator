from django.shortcuts import redirect, render

# Create your views here.
from django.http import request


def age_page(request):
    birth_day = ""

    if request.method == 'POST':
        if request.POST.get('age_submit'):
            birth_day = request.POST['birth_day']
            
            
        else:
            redirect('age_html')
            res = ""
    else:
        print("Error Occurred")

    
    return render(request, "static/age.html",
    {
     "birth_day" : birth_day
    })