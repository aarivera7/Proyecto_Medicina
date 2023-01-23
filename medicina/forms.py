from django.forms import ModelForm

from medicina.models import *


class SurgeryForm(ModelForm):
    class Meta:
        model = Surgery
        fields = ['user_id', 'speciality', 'type_surgery']


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['id_card', 'name', 'last_name', 'date_birth', 'allergies', 'medical_family_history',
                  'blood_type', 'phone_number', 'id_history']
