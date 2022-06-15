from django.shortcuts import render
from .calculator import calculate_fare
from .forms import JourneyForm
from .models import Journey
from django.http import HttpResponseRedirect

def index(request):
    print(request.method)
    if request.method == 'POST':
        form = JourneyForm(request.POST)
        if form.is_valid():
            distance = form.cleaned_data['distance']
            time = form.cleaned_data['time']
            if distance > 0:
                fare = calculate_fare(distance,time)
                print(fare)
                journey = Journey(distance=distance,time=time,fare=fare)
                journey.save()
                form = JourneyForm()
                return render(request,'index.html',{'form':form,'fare':fare})
            else:
                print('Distance must be greater than 0')
           
    form = JourneyForm()
    return render(request,'index.html',{'form':form})
