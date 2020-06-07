from django                     import forms
from django.forms               import ModelForm
from Registro.models            import Registros_traz
from django.core.exceptions     import ValidationError

################################################
#               fomulario de contacto          #
################################################                                                   
class ContactForm(forms.Form):
    asunto = forms.CharField(label='Asunto',max_length=100)
    mensaje = forms.CharField(label='Mensaje',widget=forms.Textarea)
    remitente = forms.EmailField(label='Ingrese su correo')
    copia_a_mi = forms.BooleanField(label='Marque para recibir una copia del mensaje',required=False)

################################################
#               fomulario de prueba            #
################################################   

class nombreform(forms.Form):
    su_nombre = forms.CharField(label='Su nombre',max_length=100)


#transacciones CAE  es la segunda tabla de la base de datos donde se registran las incidencias ocurridas en el centro de acopio de la exportadora

#################################################################
#  transacciones del centro de acopio de la exportadora         #
################################################################# 

class cae_modelform(ModelForm):
    class Meta:
        model   =   Registros_traz
        fields  =   [
            'centro_acopio_opciones',
            'cedula_productor', 
            'cedula_vendedor',
            'certificacion_opciones',
            'Tipo_certificacion_opciones',
            'Tipo_cacao_opciones',
            'Tipo_especialidad_opciones',
            'estado_cacao_opciones',
            'fecha_compra_venta',
            'fecha_inicio_cosecha',
            'fecha_fin_cosecha',
            'fermentacion_lote',
            'tipo_fermentacion_opciones',
            'tiempo_fermentacion',
            'tipo_secado_opciones',
            'modo_secado_opciones',
            'tiempo_secado',
            'tipo_transporte_opciones',
            'peso_lote',
            'peso_lote_calificado',
            'precio_lote_qq',
            'secado_en_cac_opciones',
            'tipo_secado_cac_opciones',
            'modo_secado_cac_opciones',
            'tiempo_secado_cac',
            'tipo_transporte_cac_opciones',
            'transportista_cac',
            # CAE
            'fermentacion_cae_lote',
            'tipo_fermentacion_cae_opciones',
            'tiempo_cae_fermentacion',
            'tipo_secado_cae_opciones',
            'modo_secado_cae_opciones',
            'tiempo_cae_secado',
            ]