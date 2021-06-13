from django.shortcuts import get_object_or_404, render

from .models import Spinner
# from .models import Question

def index(request):
    artikel = request.POST.get('artikel')
    s = Spinner()
    hasil = s.spinner(artikel)
    context = {
        'title': 'My App',
        'artikel': artikel,
        'hasil': hasil,
    }
    return render(request, 'index.html', context)