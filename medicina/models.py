from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Surgery(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=30, null=False)
    type_surgery = models.CharField(max_length=40, null=False)
    reason_surgery = models.CharField(max_length=200)
    surgery_urgency = models.IntegerField()
    date = models.DateTimeField()
    is_derived = models.BooleanField(default=False)


class Patient(models.Model):
    id_card = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=80, null=False)
    last_name = models.CharField(max_length=80, null=False)
    date_birth = models.DateField(null=False)
    blood_type = models.CharField(max_length=4, null=False)
    phone_number = models.CharField(max_length=16)
    allergies = models.CharField(max_length=80, default='Ninguna')
    id_history = models.CharField(max_length=15)
    medical_family_history = models.CharField(max_length=200)


class MedicalCare(models.Model):
    id_card = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    datetime = models.DateTimeField()
    hasBracelet = models.BooleanField()
    receivedAttention = models.BooleanField()


class Talk(models.Model):
    topic = models.CharField(max_length=50)
    observations = models.CharField(max_length=250)
    date = models.DateTimeField()
    patients = models.ManyToManyField(Patient, related_name='patients')


class SurgeryEspecial(models.Model):
    specialty = models.CharField(max_length=20)
    name = models.CharField(max_length=20)


class PhotoProfile(models.Model):
    id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    photo = models.BinaryField


class HealthProfessional(models.Model):
    id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)


class Training(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)


class ScheduledTraining(models.Model):
    id_training = models.ForeignKey(Training, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    was_finished = models.BooleanField
    health_professionals = models.ManyToManyField(HealthProfessional, related_name='professionals')

"""
class Operating_Room(models.Model):
    numberRoom = models.IntegerField(max_length=3,)


class SurgeryEquipment(models.Model):
    name = models.CharField(max_length=25, null=False)
    state = models.CharField(max_length=1, null=False)
    assignedOperatingRoom = models.ForeignKey(Operating_Room, on_delete=models.CASCADE)
    
"""
