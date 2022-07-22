from django.shortcuts import redirect, render
from .models import Concurs,Participant
from .forms import RegisterForm
from django.core.mail import send_mail, BadHeaderError
import Science_Fest.settings as settings
from django.http import HttpResponse
def main(request):
    concurs = Concurs.objects.latest('id')
    form = RegisterForm()
    return render(request, 'index.html', {"concurs":concurs,'form': form})

def participant(request):
    if request.user.is_authenticated:
        participants = Participant.objects.all().order_by("-id")
        return render(request,'participants.html',{"participants":participants})
    else:
        return redirect("main")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            new_participant = Participant(
                fest_id=Concurs.objects.latest('id'),
                surname = form.cleaned_data['surname'],
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'])

            new_participant.save()
            try:
                send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, [form.cleaned_data['email']])
            except :
                return HttpResponse('Такого электронного почтового ящика не существует.')
            return redirect('main')
    elif request.method=='GET':
        return redirect('main')

