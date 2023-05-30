from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def register_request(request):
    """
       This function handles the user registration request.

       If the request method is POST, it validates the registration form.
       If the form is valid, it creates a new user, logs them in, and redirects them to the login page.
       If the form is invalid, it displays an error message.
       If the request method is GET, it renders the registration page.

       Parameters:
           request (HttpRequest): The request object.

       Returns:
           HttpResponse: The rendered response.
       """
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("user_auth:login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    """
        This function handles the user login request.

        If the request method is POST, it validates the login form.
        If the form is valid, it authenticates the user, logs them in, and redirects them to the index page.
        If the form is invalid, it displays an error message.
        If the request method is GET, it renders the login page.

        Parameters:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: The rendered response.
        """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f" Welcome {username}.")
                return redirect("/index")
            else:
                messages.error(request, "Invalid username or password!")
        else:
            messages.error(request, "Invalid username or password!")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    """
        This function handles the user logout request.

        Logs out the user and redirects them to the home page.

        Parameters:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: The rendered response.
        """
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")
