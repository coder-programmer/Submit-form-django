from django.shortcuts import render
from .models import Submit
from .forms import SubmitForm


def index(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST)

        if form.is_valid():
            new_submit = Submit(name=request.POST['name'], last=request.POST['last'])
            new_submit.save()



    else:
        form = SubmitForm()


    context = {'form' : form }
    return render (request, 'submit/contact.html', context)