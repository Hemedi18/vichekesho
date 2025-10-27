from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as AuthLoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def register(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in directly after registration.
            login(request, user)
            return redirect('vichekesho_app:home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

class CustomLoginView(AuthLoginView):
    """Custom login view to use our own template."""
    template_name = 'users/login.html'
    # You can add more customizations here if needed

@login_required
def account_view(request):
    """Display the main account page."""
    return render(request, 'users/account.html')

class CustomPasswordChangeView(PasswordChangeView):
    """View for changing password, with custom template and success URL."""
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('users:password_change_done')