from django.contrib.auth.views import LoginView, LogoutView


class UserAccountLoginView(LoginView):
    template_name = 'login.html'
