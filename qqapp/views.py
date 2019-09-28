from django.shortcuts import render
from .models import Qq
from django.utils import timezone
from fuzzywuzzy import fuzz

# Create your views here.
def qq_list(request):
    qqs = Qq.objects.all
    return render(request, 'qqapp/qq_list.html', {'qqs' : qqs})

def search(request):
    qqsearch = Qq.objects.filter(qqname__contains=request.GET.get('q', ''))
    return render(request, 'qqapp/qqresults.html', {'qqsearch' : qqsearch})