from django.shortcuts import render
from .models import Polls

# Create your views here.
def test(request):
    context = {
        "polls": Polls.objects.all()
    }

    return render(request, 'test.html', context)