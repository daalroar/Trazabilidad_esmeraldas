import  django_tables2                  as       tables
from    .models                         import   Registros_traz


class Registros_traz_Table(tables.Table):

    id = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    cedula_productor = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    centro_acopio_opciones = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    #certificacion_opciones = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    Tipo_certificacion_opciones = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    fecha_compra_venta = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    peso_lote_calificado = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    contrato_exp = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    factura_exp = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    lote_exp = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    numero_contenedores_exp = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    numero_sacos_exp = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    total_kgs_n_exp = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    fecha_embarque_exp = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    precio_fob_tm_exp = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    franquicia_exp = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    cliente_exp = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    fecha_sal_emb_exp = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    fecha_arr_emb_exp = tables.Column(attrs={"th": {"bgcolor": "white","style":"color:green"},"td":{"bgcolor": "white","style": "color:green"}})
    
   
    class Meta:
        model = Registros_traz
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = (
            'id',
            'centro_acopio_opciones',
            'cedula_productor', 
            #'cedula_vendedor',
            #'certificacion_opciones',
            'Tipo_certificacion_opciones',
            #'Tipo_cacao_opciones',
            #'Tipo_especialidad_opciones',
            #'estado_cacao_opciones',
            'fecha_compra_venta',
            #'fecha_inicio_cosecha',
            #'fecha_fin_cosecha',
            #'fermentacion_lote',
            #'tipo_fermentacion_opciones',
            #'tiempo_fermentacion',
            #'tipo_secado_opciones',
            #'modo_secado_opciones',
            #'tiempo_secado',
            #'tipo_transporte_opciones',
            #'peso_lote',
            'peso_lote_calificado',
            #'precio_lote_qq',
            #'secado_en_cac_opciones',
            #'tipo_secado_cac_opciones',
            #'modo_secado_cac_opciones',
            #'tiempo_secado_cac',
            #'tipo_transporte_cac_opciones',
            #'transportista_cac',
        #   CAE 27
            #'fermentacion_cae_lote',
            #'tipo_fermentacion_cae_opciones',
            #'tiempo_cae_fermentacion',
            #'tipo_secado_cae_opciones',
            #'modo_secado_cae_opciones',
            #'tiempo_cae_secado',
        #exportadora 33
            'contrato_exp',
            'factura_exp',
            'lote_exp',
            'numero_contenedores_exp',
            'numero_sacos_exp',
            #'total_kgs_b_exp',
            'total_kgs_n_exp',
            'fecha_embarque_exp',
            #'posiciones_exp_opciones',
            'precio_fob_tm_exp',
            'franquicia_exp',
            'cliente_exp',
            'fecha_sal_emb_exp',
            'fecha_arr_emb_exp',
        ) 