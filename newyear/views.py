from django.shortcuts import render
from datetime import datetime
# Create your views here.

def index(request):
    date = datetime.now()
    if date.month == 2 and date.day == 19:
        return render(request, "newyear/index.html", {"year":"Yes"})
    else:
        return render(request, "newyear/index.html", {"year":"No"})
     