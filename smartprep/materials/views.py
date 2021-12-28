from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from accounts.auth import learner_only

@learner_only
@login_required
def home(request):
    return render(request, 'materials/home.html')