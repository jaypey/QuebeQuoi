from django.shortcuts import render

# Create your views here.
def qq_list(request):
    return render(request, 'qqapp/qq_list.html', {})