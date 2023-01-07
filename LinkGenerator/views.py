from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def home(request):

    if request.method == 'POST':
        number = request.POST['number']
        message = request.POST['message']

        new_message = message.replace(' ', '%20')
        link = 'http://wa.me/{}?text={}'.format(number, new_message)

        return HttpResponseRedirect(link)

    return render(request, 'index.html')