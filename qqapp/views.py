from django.shortcuts import render, get_object_or_404
from .models import Qq
from django.utils import timezone

# Create your views here.
def qq_list(request):
    qqs = Qq.objects.all
    return render(request, 'qqapp/qq_list.html', {'qqs' : qqs})

def search(request):
    qqsearch = Qq.objects.filter(qqname__contains=request.GET.get('q', ''))
    return render(request, 'qqapp/qqresults.html', {'qqsearch' : qqsearch})

def qqdetail(request, pk):
    qq = get_object_or_404(Qq, pk=pk)
    return render(request, 'qqapp/qq_detail.html', {'qq' : qq})

def about(request):
    return render(request, 'qqapp/qq_about.html')