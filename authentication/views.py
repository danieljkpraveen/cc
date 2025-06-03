from django.shortcuts import (
    render,
    redirect
)

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = SignUpForm()
    return render(request, 'authentication/signup.html', {'form': form})
