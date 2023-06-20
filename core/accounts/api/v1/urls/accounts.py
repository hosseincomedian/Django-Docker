from django.urls import include, path
from accounts.api.v1 import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'api-v1'

urlpatterns = [
    #registration
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    
    #change password
    path('change-password/', views.ChangePasswordApiView.as_view(), name='change-password'),
    #reset password
    #login token
    path('token/login/', views.CustomAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout'),

    #login jwt
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),

    
]
