from django.shortcuts import render
from infoschoolpupil.models import PupilMoney

def all_info(request):
    info = PupilMoney.objects.all().order_by('-id')
    context={
        'info': info
    }
    return render(request, 'all_info.html', context)
