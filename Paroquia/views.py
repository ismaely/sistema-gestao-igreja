from Config.includes import *

# Create your views here.


def registar_cadastro_paroquia(request):
    context = {}
    return render (request, 'paroquia/registar_cadastro_paroquia.html', context)

