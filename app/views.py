from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Me, Port, Service, Test, Message
from .forms import MsgForm
# Create your views here.
def index(request):
    person = Me.objects.filter()
    port = Port.objects.all()
    service = Service.objects.all()
    tests = Test.objects.all()
    if request.method == 'POST':
        forms = MsgForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
        
    else:
        forms = MsgForm()
    context = {
        'persons':person,
        'ports':port,
        'services':service,
        'tests':tests,
        'forms':forms
    }
    return render(request, 'index.html', context)


