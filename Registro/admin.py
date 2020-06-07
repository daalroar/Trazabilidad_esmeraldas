from django.contrib import admin

# Register your models here.

# Para regristrar los modelos se sigue el esquema: from myproject.myapp.models import Tablas

from Registro.models import Registros_traz

""" la siguiente linea permite mirar como una tabla 
los registros en el adminsitrador """



#la siguiente linea permite registrar en las tablas desde el administrador de django

class Registros_traz_Admin (admin.ModelAdmin):
    fieldsets = (

        (None, {
            'fields': (
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
                )
        }),
        
        
        ('Informacion transaccion', {
            'classes': ('collapse',),
            'fields':  ('peso_lote', 'peso_lote_calificado','precio_lote_qq'),
        }),

        ('Secado en Centro de Acopio Comunitario', {
            'classes': ('collapse',),
            'fields':  ('secado_en_cac_opciones','tipo_secado_cac_opciones','modo_secado_cac_opciones','tiempo_secado_cac'),
        }),

        ('Transporte Centro Acopio Comunitario a Centro de Acopio Exportadora', {
            'classes': ('collapse',),
            'fields':  ('tipo_transporte_cac_opciones','transportista_cac'),
        }),

        ('Registros Centro Acopio Exportadora', {
            'classes': ('collapse',),
            'fields':  ('fermentacion_cae_lote','tipo_fermentacion_cae_opciones','tiempo_cae_fermentacion','tipo_secado_cae_opciones','modo_secado_cae_opciones','tiempo_cae_secado'),
        }),


        ('Registros Exportadora', {
            'classes': ('collapse',),
            'fields':  ('contrato_exp','factura_exp','lote_exp','numero_contenedores_exp','numero_sacos_exp','total_kgs_b_exp','total_kgs_n_exp','fecha_embarque_exp','posiciones_exp_opciones','precio_fob_tm_exp','franquicia_exp','cliente_exp', 'fecha_sal_emb_exp','fecha_arr_emb_exp'),
        }),


    )
    list_display=(
        "centro_acopio_opciones",
        "cedula_productor",
        "Tipo_certificacion_opciones",
        "Tipo_cacao_opciones",
        "fecha_compra_venta",
        "peso_lote",
        "peso_lote_calificado",
        "precio_lote_qq"
        )
    list_filter=(
        "centro_acopio_opciones",
        "certificacion_opciones",
        "Tipo_certificacion_opciones",
        "Tipo_cacao_opciones",
        "Tipo_especialidad_opciones",
        "estado_cacao_opciones",
        "fecha_compra_venta",
        "fecha_inicio_cosecha",
        "fecha_fin_cosecha",
        "fermentacion_lote",
        "tipo_fermentacion_opciones",
        "tiempo_fermentacion",
        "tipo_secado_opciones",
        "modo_secado_opciones",
        "tiempo_secado",
        "tipo_transporte_opciones",
        "secado_en_cac_opciones",
        "tipo_secado_cac_opciones",
        'modo_secado_cac_opciones',
        )
    date_hierarchy="fecha_compra_venta"
    search_fields=("centro_acopio_opciones",'cedula_productor',)

admin.site.register(Registros_traz,Registros_traz_Admin)

