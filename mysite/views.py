from re import A
from django.shortcuts import get_object_or_404, render

# from .models import Spinner
from spinner.models import Words
# from .models import Question

def index(request):
    artikel = request.POST.get('artikel')
    s = Words()
    hasil_word = s.spinWord(artikel)
    hasil = s.spinNegative(hasil_word)
    context = {
        'title': 'My App',
        'artikel': artikel,
        'hasil': hasil,
    }
    return render(request, 'index.html', context)