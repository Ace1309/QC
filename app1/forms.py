from .models import CallCheck
from django.forms import ModelForm, TextInput, SelectDateWidget, NumberInput, Textarea


class CallCheckForm(ModelForm):
    class Meta:
        model = CallCheck
        fields = [
            'operator',
            'qc_manager',
            'op_team',
            'call_date',
            'check_up_date',
            'call_type',
            'call_duration',
            'project',
            'phone_number',
            'record_name',
            'intro',
            'presentation',
            'purpose',
            'info_to_debtor',
            'payment_options',
            'objections_handling',
            'commitment_closing',
            'farewell',
            'ant_event_result',
            'ant_info',
            'call_model_following',
            'voice_tone',
            'prohibited_phrases',
            'comments'
            ]

        widgets = {
            "call_date": SelectDateWidget(attrs={
                'class': 'call-info',
                'placeholder': 'Choose date'
            }),
            "check_up_date": SelectDateWidget(attrs={
                'class': 'call-info',
                'placeholder': 'Choose date'
            }),
            "call_duration": NumberInput(attrs={
                'class': 'call-info',
                'placeholder': 'Ingrese la duración de la llamada en segundos'
            }),
            "phone_number": NumberInput(attrs={
                'class': 'call-info',
                'placeholder': 'Ingrese el número de teléfono del deudor'
            }),
            "record_name": TextInput(attrs={
                'class': 'call-info',
                'placeholder': 'Ingrese el nombre del archivo de la llamada'
            }),
            "comments": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Añadir cualquier comentario'
            })

        }