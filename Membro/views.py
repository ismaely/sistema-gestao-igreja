from Config.includes import *

# Create your views here.




def registar_cadastro_membro(request):
    context = {}
    return render (request, 'membro/registar_cadastro_membro.html', context)

