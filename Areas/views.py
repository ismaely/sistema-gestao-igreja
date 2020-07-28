from Config.includes import *

# Create your views here.


def registar_cadastro_area(request):
    context = {}
    return render (request, 'areas/registar_cadastro_area.html', context)

