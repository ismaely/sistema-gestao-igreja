from Config.includes import *

# Create your views here.

def login_utilizador(request):
    context = {}
    return render (request, 'utilizador/login.html', context)

