from django.shortcuts import render, redirect
from User.Infrastructure.PostgreUserRepository import PostgreUserRepository
from User.Application.UserRegistrationService import UserRegistrationService

postgreUserRepository = PostgreUserRepository()
userRegistrationService = UserRegistrationService(postgreUserRepository)


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            userRegistrationService.registerUser(username, email, password)
            return redirect('register')  # Redirigir a una página de éxito
        except ValueError as e:
            return render(request, 'register.html', {'error': str(e)})

    return render(request, 'register.html')