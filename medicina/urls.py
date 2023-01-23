from django.urls import path
from medicina.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('recover/', recover_account, name='recover'),
    path('code/', code),
    path('changepasswordr/', change_password_r),
    path('changepassword/', change_password, name='change_password'),
    path('home/', home, name='home'),
    path('editprofile/', edit_profile, name='edit_profile'),
    path('indicators/', indicators, name='indicators'),
    path('createpatient/', create_patient, name='create_patient'),
    path('schedulesurgery/', create_surgery, name='schedule_surgery'),
    path('listpatient/', list_patients, name='list_patient'),
    path('listsurgery/', list_surgery, name='list_surgery'),
    path('sugertySpecial/', list_surgery_especial, name='list_surgeryEspecial'),
    path('logout/', logout_view, name='logout'),
    # Con template_name dentro de as.view se puede personalizar el html
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_send.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"),
         name="password_reset_complete"),
]
