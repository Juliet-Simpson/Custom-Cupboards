from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cupboards.models import Cupboard

# Create your views here.

def my_cupboards(request):

    return render(request, 'profiles/my_cupboards.html')

