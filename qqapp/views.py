from django.shortcuts import render, get_object_or_404, redirect
from .models import Qq, RegisterForm
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

def register(request):
    if request.method == 'post':
        form = RegisterForm(request.post)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html')