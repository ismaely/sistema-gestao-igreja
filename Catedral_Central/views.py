from Config.includes import *


# Create your views here.

def home_central(request):
    context = {}
    return render (request, 'catedral/index_central.html', context)

