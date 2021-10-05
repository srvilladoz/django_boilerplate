from django.views.generic.edit import CreateView

from accounts.forms import CustomUserCreationForm


class SignUpView(CreateView):
    form = CustomUserCreationForm
    template_name = "registration/signup.html"
