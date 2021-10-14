from django.urls import path
from .views.auth import RegisterView,VerifyEmail,LoginAPIView,LogoutAPIView,register,home
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns =[
    path('',home,name = 'home'),
    path('register',register,name ='register'), 
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
# path('register', RegistrationView.as_view(), name="register"),  
#     path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
#          name="validate-username"),
#     path('validate-email', csrf_exempt(EmailValidationView.as_view()),
#          name='validate_email'),
#     path('activate/<uidb64>/<token>',
#          VerificationView.as_view(), name='activate'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)