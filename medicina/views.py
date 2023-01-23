from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.db.models import Q
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'index.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        print(request.POST)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'El usuario o la contraseña son incorrectas'
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': error})

    return render(request, 'login.html', {'login': AuthenticationForm, 'error': ''})


def recover_account(request):
    return render(request, 'password/recuperacionCuenta.html')


def code(request):
    return render(request, 'password/recuperacionContrasenia.html')


def change_password_r(request):
    return render(request, 'password/cambioContrasenia.html', {'form': PasswordChangeForm('prueba')})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
        else:
            return render(request, 'password/change_password.html', {
                'form': PasswordChangeForm(request.user),
                'error': form.errors
            })
    return render(request, 'password/change_password.html', {'form': PasswordChangeForm(request.user)})


@login_required
def home(request):
    return render(request, 'mostrarPerfil.html', {'name': 'María'})


@login_required
def edit_profile(request):
    return render(request, 'editarPerfil.html', {'name': 'María'})


@login_required
def indicators(request):
    return render(request, 'Indicadores.html')


@login_required
def create_patient(request):
    if request.method == 'POST':
        id_card1 = request.POST["id_card"]
        name1 = request.POST["name"]
        last_name1 = request.POST["last_name"]
        date_birth1 = request.POST["date_birth"]
        blood_type1 = request.POST["blood_type"]
        phone_number1 = request.POST["phone_number"]
        allergies1 = request.POST["allergies"]
        id_history1 = request.POST["id_history"]
        medical_family_history1 = request.POST["medical_family_history"]

        patient = Patient(id_card=id_card1, name=name1, last_name=last_name1, date_birth=date_birth1,
                          blood_type=blood_type1, phone_number=phone_number1, allergies=allergies1, id_history=id_history1,
                          medical_family_history=medical_family_history1)
        patient.save()
    return render(request, 'creacionPaciente.html', {'form': PatientForm})


@login_required
def create_surgery(request):
    if request.method == 'POST':
        id_card1 = request.POST["id_card"]
        name1 = request.POST["name"]
        last_name1 = request.POST["last_name"]
        date_birth1 = request.POST["date_birth"]
        blood_type1 = request.POST["blood_type"]
        phone_number1 = request.POST["phone_number"]
        allergies1 = request.POST["allergies"]
        id_history1 = request.POST["id_history"]
        medical_family_history1 = request.POST["medical_family_history"]

        patient = Patient(id_card=id_card1, name=name1, last_name=last_name1, date_birth=date_birth1,
                          blood_type=blood_type1, phone_number=phone_number1, allergies=allergies1, id_history=id_history1,
                          medical_family_history=medical_family_history1)
        patient.save()
    return render(request, 'programarCirugia.html')


@login_required
def list_surgery_especial(request):
    total = SurgeryEspecial.objects.all()
    return render(request, 'cirujiasEspecialidad.html.html', {'total': total})


@login_required
def list_patients(request):
    search = request.POST.get("buscar")
    paciente_r = Patient.objects.all()
    if search:
        paciente_r = Patient.objects.filter(
            Q(name__contains=search) |
            Q(id_card__contains=search) |
            Q(last_name__contains=search)
        ).distinct()
    return render(request, 'listadoPacientes.html', {'paciente_r': paciente_r})


@login_required
def list_surgery(request):
    search = request.POST.get("buscar")
    surgery = Surgery.objects.all()
    if search:
        surgery = Surgery.objects.filter(
            Q(speciality__contains=search) |
            Q(reason_surgery__contains=search) |
            Q(type_surgery__contains=search) |
            Q(surgery_urgency__contains=search)
        ).distinct()
    return render(request, 'listaCirugias.html', {'surgeries': surgery})


def logout_view(request):
    logout(request)
    return redirect('index')

