from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import NewProfileForm
from django.db import models
import uuid


# Create your views here.
def index(request):
    return render(request,"core/index.html")

@login_required
def ProfileList(request):
    profiles = Profile.objects.all()
    return render(request,"profilelist.html",{
        "profiles" : profiles,
    })

@login_required
def new_profile(request):
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)

        if form.is_valid():
            new_profile = form.save(commit=False)
            #new_profile.uuid = models.UUIDField(default=uuid.uuid4)
            new_profile.save()
            return redirect("core:profiles")
    else:
        form = NewProfileForm()

    return render(request, 'form.html', {
        'form': form,
    })

