from Config.includes import *

# Create your views here.


def registar_cadastro_tribo(request):
    context = {}
    return render (request, 'tribos/registar_cadastro_tribo.html', context)

