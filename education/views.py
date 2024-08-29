from django.shortcuts import render

# Create your views here.


def education(request):
    context = {'skils': 'active'}
    return render(request, 'education/skils.html', context)
