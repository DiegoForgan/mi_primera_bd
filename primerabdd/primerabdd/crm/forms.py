from .models import Organizacion, Cuenta, Contacto, Voluntario, Oportunidad, CampoCustomOrigen, CampoCustomTipoContacto, CampoCustomTipoCuenta, CampoCustomTipoOportunidad, CampoCustomEstadoOportunidad
from django import forms
from django.forms import ModelForm, CheckboxInput


from django_select2.forms import Select2Widget

class DateInput(forms.DateInput):
    input_type = 'date'

class ContactoCrearForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'


        widgets = {
            'cuenta': Select2Widget(attrs={'data-placeholder':"Vacío para crear cuenta nueva"}),
            'origen': Select2Widget(attrs={'data-placeholder':""}),
            'categoria': Select2Widget(attrs={'data-placeholder':""}),
            'sexo': Select2Widget(attrs={'data-placeholder':""}),
            'fecha_de_nacimiento': DateInput(),
            'estado': Select2Widget(attrs={'data-placeholder':"Estado"}),
            'turno': Select2Widget(attrs={'data-placeholder':"Turno"}),
            'habilidades': Select2Widget(attrs={'data-placeholder':"Habilidades"}),
            'pais': Select2Widget(attrs={'data-placeholder':"Pais"}),

        }

    def __init__(self, *args, **kwargs):
        super(ContactoCrearForm, self).__init__(*args, **kwargs)

class CuentaCrearForm(ModelForm):
    class Meta:
        model = Cuenta
        exclude = ['organizacion']

        widgets = {
            'tipo': Select2Widget(attrs={'data-placeholder':""}),
        }

    def __init__(self, *args, **kwargs):
        super(CuentaCrearForm, self).__init__(*args, **kwargs)

class OportunidadCrearForm(ModelForm):
    class Meta:
        model = Oportunidad
        fields = '__all__'

        widgets = {
            'tipo': Select2Widget(attrs={'data-placeholder':"Tipo"}),
            'estado_oportunidad': Select2Widget(attrs={'data-placeholder':"Estado"}),
            'cuenta': Select2Widget(attrs={'data-placeholder':"Cuenta"}),
            'fecha': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(OportunidadCrearForm, self).__init__(*args, **kwargs)

class CampoCustomCrearOrigenForm(ModelForm):
    class Meta:
        model = CampoCustomOrigen
        exclude = ['organizacion']

    def __init__(self, *args, **kwargs):
        super(CampoCustomCrearOrigenForm, self).__init__(*args, **kwargs)

class CampoCustomCrearTipoContactoForm(ModelForm):
    class Meta:
        model = CampoCustomTipoContacto
        exclude = ['organizacion']

    def __init__(self, *args, **kwargs):
        super(CampoCustomCrearTipoContactoForm, self).__init__(*args, **kwargs)

class CampoCustomCrearTipoCuentaForm(ModelForm):
    class Meta:
        model = CampoCustomTipoCuenta
        exclude = ['organizacion']

    def __init__(self, *args, **kwargs):
        super(CampoCustomCrearTipoCuentaForm, self).__init__(*args, **kwargs)

class CampoCustomCrearEstadoOportunidadForm(ModelForm):
    class Meta:
        model = CampoCustomEstadoOportunidad
        exclude = ['organizacion']

        widgets={
            'estado': forms.TextInput(attrs={'id': 'estado_custom_oportunidad'})
        }
        

    def __init__(self, *args, **kwargs):
        super(CampoCustomCrearEstadoOportunidadForm, self).__init__(*args, **kwargs)

class CampoCustomCrearTipoOportunidadForm(ModelForm):
    class Meta:
        model = CampoCustomTipoOportunidad
        exclude = ['organizacion']

    def __init__(self, *args, **kwargs):
        super(CampoCustomCrearTipoOportunidadForm, self).__init__(*args, **kwargs)



