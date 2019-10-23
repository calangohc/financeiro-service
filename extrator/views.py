from django.shortcuts import render

# Create your views here.

def file_list(request):
    return render(request, 'extrator/file_list.html', {})
