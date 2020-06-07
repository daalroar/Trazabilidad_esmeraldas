from    django.db                   import      models
from    django.forms                import      ModelForm
from    django.core.validators      import      MaxValueValidator, MinValueValidator


# Clase para registrar las transacciones de compra venta en el centro de acopio numero, el que esta mas cercano al productor

class Registros_traz(models.Model):
    #constantes que definen opciones
    TIMBIRE = 'TM'
    BORBON = 'BR'
    COLON_ELOY= 'CE'
    SAN_GREGORIO = 'SG'

    CENTRO_ACOPIO_1_CHOICES = [
        (TIMBIRE, 'Timbire'),
        (BORBON ,'Borbon'),
        (COLON_ELOY, 'Colon Eloy'),
        (SAN_GREGORIO, 'San Gregorio'),
    ]
    # el campo se llama centro_acopio opciones para consultas y plantillas
    centro_acopio_opciones = models.CharField(
        max_length=2,
        choices=CENTRO_ACOPIO_1_CHOICES, #Un grupo de valores de selección para este campo.
        default=SAN_GREGORIO, #valor por defecto del campo
    )
       
    # campo para registrar el id del productor del lote de cacao que se entrega
    cedula_productor = models.CharField(
        max_length=10,
        help_text="Ingrese numero de cedula del producto",
        default="",
        null=True
    )
        
    #campo para registrar el id del vendedor (en caso de que exista un comercialnte o trasnpotista)
    cedula_vendedor = models.CharField(
        max_length=10, 
        help_text="Ingrese numero de cedula del comercialnte o transportista",
        default="na",
        null=True
    )
    
    #campo para determinar si tiene alguna certificacion
    
    SI ='Si'
    NO = 'No'
    TRANSICION='Transición'


    Certificacion_choices = [
        (SI, 'Si'),
        (NO,'No'),
        (TRANSICION, 'En procesos de transición'),
    ]
    # campo de eleccion de si se tiene o no certificacio
    certificacion_opciones = models.CharField(
        max_length=10,
        choices=Certificacion_choices, #Un grupo de valores de selección para este campo.
        default=SI, #valor por defecto del campo
        null=True
    )
    
    #############################################
    #                                           #
    # campo de seleccion de tipo de certificacion
    #                                           #
    #############################################

    Org ='Organica'
    Flo = 'Comercio Justo / Fair Trade - FLO'
    Rain = 'Rain Forest'
    Nat = 'Nat'
    Spp = 'Pequeños Productores SPP'
    Otra = 'Otra'
    Noapli= 'No aplica'
    
    Tipo_certif_choices = [
        (Org, 'Organica'),
        (Flo,'Comercio Justo / Fair Trade - FLO'),
        (Rain,'Rain Forest'),
        (Nat,'Naturland'),
        (Spp,'Pequeños Productores SPP'),
        (Otra,'Otra'),
        (Noapli,'No aplica'),
        
    ]

    Tipo_certificacion_opciones = models.CharField(
        max_length=100,
        choices=Tipo_certif_choices, #Un grupo de valores de selección para este campo.
        default=Org, #valor por defecto del campo
        null=True
    )
    #############################################
    #                                           #
    # campo de seleccion tipo de cacao genetico #
    #                                           #
    #############################################

    Nac ='Nacional'
    CCN = 'CCN-51'
    Criollo = 'Criollo'
    Mezclado = 'Mix de variedades'
    Otro = 'Otro'
    
    Tipo_cacao_choices = [
        
        (Nac, 'Nacional'),
        (CCN,'CCN-51'),
        (Criollo,'Criollo'),
        (Mezclado,'Mix de variedades'),
        (Otro,'Otro'),
        
    ]

    Tipo_cacao_opciones = models.CharField(
        max_length=100,
        choices=Tipo_cacao_choices, #Un grupo de valores de selección para este campo.
        default=Nac, #valor por defecto del campo
        null=True
    )
    #############################################
    #                                           #
    #       campo tipo de especialidad          #
    #                                           #
    #############################################

    Gen = 'Genetica'
    Org = 'Origen'
    Tra = 'Tratamiento'
    Sab = 'Organoléptica'
    Otro = 'Otro'
    
    Tipo_especialidad_choices = [
        
        (Gen,'Genetica'),
        (Org,'Origen'),
        (Tra,'Tratamiento'),
        (Sab,'Organoléptica'),
        (Otro,'Otro'),
        
    ]

    Tipo_especialidad_opciones = models.CharField(
        max_length=100,
        choices=Tipo_especialidad_choices, #Un grupo de valores de selección para este campo.
        default=Org, #valor por defecto del campo
        null=True
    )
    #############################################
    #                                           #
    #       campo estado de cacao entregado     #
    #                                           #
    #############################################

    Sec = 'Seco, humedad <2%'
    Sem = 'Semiseco humedad entre 15% al 20%' 
    Bab = 'Humedad superior al 20%'
    Mix = 'Lote con diferentes grados de humedad'
    Otr = 'Otro'
    
    estado_cacao_choices = [
        
        (Sec,'Seco, humedad <2%'),
        (Sem,'Semiseco humedad entre 15% al 20%'),
        (Bab,'Humedad superior al 20%'),
        (Mix,'Lote con diferentes grados de humedad'),
        (Otr,'Otro'),
        
    ]

    estado_cacao_opciones = models.CharField(
        max_length=100,
        choices=estado_cacao_choices, #Un grupo de valores de selección para este campo.
        default=Sec, #valor por defecto del campo
        null=True
    )
    #########################################################
    #                                                       #
    #  Fecha de entrega al Centro de Acopio Comunitario     #
    #                                                       #
    #########################################################

    fecha_compra_venta = models.DateField(null=True, blank=True)

    #########################################################
    #                                                       #
    #  Fechas de inicion y final de la cosecha              #
    #  correspondiente al lote entregado                    #
    #                                                       #
    #                                                       #
    #########################################################

    fecha_inicio_cosecha = models.DateField (null=True, blank=True)
    fecha_fin_cosecha = models.DateField(null=True, blank=True)
    #########################################################
    #                                                       #
    #     se hizo fermentacion?                             #
    #                                                       #
    #########################################################
    SI ='Si'
    NO ='No'
    fermentacion_choices = [
        (SI, 'Si'),
        (NO,'No'),
    ]
    fermentacion_lote = models.CharField(
        max_length=10,
        choices=fermentacion_choices, #Un grupo de valores de selección para este campo.
        default=SI, #valor por defecto del campo
        null=True
    )

    #########################################################
    #                                                       #
    #     Tipo de fermentación                              #
    #                                                       #
    #########################################################
    Sac = 'Saco'
    Caj = 'Caja de fermentación' 
    Lon = 'Lona'
    Otr = 'Otro'
    tipo_fermentacion_choices = [
        (Sac,'Saco'),
        (Caj,'Caja de fermentacion'),
        (Lon,'Lona'),
        (Otr,'Otro'),
    ]
    tipo_fermentacion_opciones = models.CharField(
        max_length=100,
        choices=tipo_fermentacion_choices, #Un grupo de valores de selección para este campo.
        default=Sac, #valor por defecto del campo
        null=True
    )

    #########################################################
    #                                                       #
    #     Tiempo de fermentación                            #
    #                                                       #
    #########################################################    

    tiempo_fermentacion = models.CharField(
        max_length=20,
        null=True,
        help_text="Ingrese tiempo de fermentacion en dias y horas",
        )


    
    #########################################################
    #                                                       #
    #     Tipo de secado aplicado al lote                   #
    #                                                       #
    #########################################################
    Nin = 'Ninguno'
    Sol = 'Secado Natural con Sol' 
    Som = 'Secado Natural en sombra'
    Gas = 'Secado a gas'

    tipo_secado_choices = [
        (Nin , 'Ninguno'),
        (Sol , 'Secado Natural con Sol' ),
        (Som , 'Secado Natural en sombra'),
        (Gas , 'Secado a gas'),
    ]
    tipo_secado_opciones = models.CharField(
        max_length=100,
        choices=tipo_secado_choices, #Un grupo de valores de selección para este campo.
        default=Sol, #valor por defecto del campo
        null=True
    )

    #########################################################
    #                                                       #
    #              Modo de secado natural                   #
    #                                                       #
    #########################################################
    Lon = 'Lona'
    Mar = 'Marquesina' 
    Ban = 'Bandeja de secado'
    Ota = 'Otra'

    modo_secado_choices = [
        (Lon , 'Lona'),
        (Mar , 'Marquesina' ),
        (Ban , 'Bandeja de secado'),
        (Ota , 'Otra'),
    ]
    modo_secado_opciones = models.CharField(
        max_length=100,
        choices=modo_secado_choices, #Un grupo de valores de selección para este campo.
        default=Lon, #valor por defecto del campo
        null=True
    )

    #########################################################
    #                                                       #
    #     Tiempo de secado                                  #
    #                                                       #
    #########################################################    

    tiempo_secado = models.CharField(
        max_length=20,
        null=True,
        help_text="Ingrese tiempo del proceso de secado: dias y horas para secado natural /horas para secado a gas",
        )

    #######################################################################
    #                                                                     #
    #     Forma de transporte productor - Centro de acopio 1              #
    #                                                                     #
    #######################################################################

    Pro = 'Transporte Propio'
    Fin = 'Flete pagado individual' 
    Fco = 'Flete pagado colectivamente'
    Ott = 'Otro'

    tipo_transporte_choices = [
        (Pro , 'Transporte Propio'),
        (Fin , 'Flete pagado individual'),
        (Fco , 'Flete pagado colectivamente'),
        (Ott , 'Otro'),
    ]
    tipo_transporte_opciones = models.CharField(
        max_length=100,
        choices=tipo_transporte_choices, #Un grupo de valores de selección para este campo.
        default=Pro, #valor por defecto del campo
        null=True
    )
    #######################################################################
    #                                                                     #
    #       TRANSACCION DE VENTA A CENTRO DE ACOPIO 1                     #
    #                                                                     #
    #######################################################################

    #######################################################################
    #                                                                     #
    #         PESAJE DEL LOTE TRANSFERIDO                                 #
    #                                                                     #
    #######################################################################

    peso_lote=models.FloatField(
        null=True,
        default=0.00,
        help_text="Ingrese el peso EN LIBRAS del lote entregado por el productor/comerciante sin aplicar calificacion de humedad",
    )

    peso_lote_calificado=models.FloatField(
        null=True,
        default=0.00,
        help_text="Ingrese el peso EN LIBRAS del lote entregado por el productor/comerciante CON ESTIMACION/CALIFICACION DE HUMEDAD",
    )

    #######################################################################
    #                                                                     #
    #         VALOR PAGADO POR QUINTAL                                    #
    #                                                                     #
    #######################################################################

    precio_lote_qq=models.FloatField(
        null=True,
        default=0.00,
        help_text="Ingrese el PRECIO PAGADO  por QUINTAL",
    )

    #######################################################################
    #                                                                     #
    #       SECADO EN EL CENTRO DE ACOPIO COMUNITARIO                     #
    #                                                                     #
    #######################################################################

    Sip = 'SI'
    Nop = 'NO'

    secado_en_cac_choices = [
        (Sip , 'SI'),
        (Nop , 'NO'),
    ]
    secado_en_cac_opciones = models.CharField(
        max_length=100,
        choices=secado_en_cac_choices, #Un grupo de valores de selección para este campo.
        default=Sip, #valor por defecto del campo
        null=True
    )
 
    #######################################################################
    #                                                                     #
    #       TIPO DE SECADO EN CENTRO DE ACOPIO COMUNITARIO                #
    #                                                                     #
    #######################################################################
    
    Nin = 'Ninguno'
    Sol = 'Secado Natural con Sol' 
    Som = 'Secado Natural en sombra'
    Gas = 'Secado a gas'

    tipo_secado_cac_choices = [
        (Nin , 'Ninguno'),
        (Sol , 'Secado Natural con Sol' ),
        (Som , 'Secado Natural en sombra'),
        (Gas , 'Secado a gas'),
    ]
    tipo_secado_cac_opciones = models.CharField(
        max_length=100,
        choices=tipo_secado_cac_choices, #Un grupo de valores de selección para este campo.
        default=Sol, #valor por defecto del campo
        null=True
    )
    #########################################################
    #                                                       #
    #              Modo de secado natural en CAC            #
    #                                                       #
    #########################################################
    Lon = 'Lona'
    Mar = 'Marquesina' 
    Ban = 'Bandeja de secado'
    Ota = 'Otra'

    modo_secado_cac_choices = [
        (Lon , 'Lona'),
        (Mar , 'Marquesina' ),
        (Ban , 'Bandeja de secado'),
        (Ota , 'Otra'),
    ]
    modo_secado_cac_opciones = models.CharField(
        max_length=100,
        choices=modo_secado_cac_choices, #Un grupo de valores de selección para este campo.
        default=Lon, #valor por defecto del campo
        null=True
    )

    #########################################################
    #                                                       #
    #     Tiempo de secado                                  #
    #                                                       #
    #########################################################    

    tiempo_secado_cac = models.CharField(
        max_length=20,
        null=True,
        help_text="Ingrese tiempo del proceso de secado: dias y horas para secado natural /horas para secado a gas",
        )
    
    #######################################################################
    #                                                                     #
    #     Forma de transporte Centro de acopio 1 -Centro de acopio 2      #
    #                                                                     #
    #######################################################################

    Pro = 'Transporte Propio'
    Fin = 'Flete pagado individual' 
    Fco = 'Flete pagado colectivamente'
    Ott = 'Otro'

    tipo_transporte_cac_choices = [
        (Pro , 'Transporte Propio'),
        (Fin , 'Flete pagado individual'),
        (Fco , 'Flete pagado colectivamente'),
        (Ott , 'Otro'),
    ]
    tipo_transporte_cac_opciones = models.CharField(
        max_length=100,
        choices=tipo_transporte_cac_choices, #Un grupo de valores de selección para este campo.
        default=Pro, #valor por defecto del campo
        null=True
    )
    
    #######################################################################
    #                                                                     #
    #     Nombre transportista CAC a CAE                                  #
    #                                                                     #
    #######################################################################

    transportista_cac = models.CharField(
    max_length=20,
    null=True,
    help_text="Ingrese nombres del transportista",
    )

    #**********************************************************************************************************************************************************
    #**********************************************************************************************************************************************************
    #**********************************************************************************************************************************************************
    #
    #                                   CAMPOS DEL CENTRO DE ACOPIO DE PRIMER NIVEL DE LA EXPORTADORA
    #
    #**********************************************************************************************************************************************************
    #**********************************************************************************************************************************************************
    #**********************************************************************************************************************************************************

    ##############################################################################################
    #                                                                                            #
    #     se hizo fermentacion en centro de acopio de la exportadora                             #
    #                                                                                            #
    ##############################################################################################
    SI ='Si'
    NO ='No'
    fermentacion_cae_choices = [
        (SI, 'Si'),
        (NO, 'No'),
    ]
    fermentacion_cae_lote = models.CharField(
        max_length=10,
        choices=fermentacion_cae_choices, #Un grupo de valores de selección para este campo.
        default=SI, #valor por defecto del campo
        null=True
    )

    #########################################################
    #                                                       #
    #     Tipo de fermentación                              #
    #                                                       #
    #########################################################
    Sac = 'Saco'
    Caj = 'Caja de fermentación' 
    Lon = 'Lona'
    Otr = 'Otro'
    tipo_fermentacion_cae_choices = [
        (Sac,'Saco'),
        (Caj,'Caja de fermentacion'),
        (Lon,'Lona'),
        (Otr,'Otro'),
    ]
    tipo_fermentacion_cae_opciones = models.CharField(
        max_length=100,
        choices=tipo_fermentacion_choices, #Un grupo de valores de selección para este campo.
        default=Sac, #valor por defecto del campo
        null=True
    )

    #########################################################
    #                                                       #
    #     Tiempo de fermentación                            #
    #                                                       #
    #########################################################    

    tiempo_cae_fermentacion = models.CharField(
        max_length=20,
        null=True,
        help_text="Ingrese tiempo de fermentacion en dias y horas",
        )


    
    #########################################################
    #                                                       #
    #     Tipo de secado aplicado al lote                   #
    #                                                       #
    #########################################################
    Nin = 'Ninguno'
    Sol = 'Secado Natural con Sol' 
    Som = 'Secado Natural en sombra'
    Gas = 'Secado a gas'

    tipo_secado_cae_choices = [
        (Nin , 'Ninguno'),
        (Sol , 'Secado Natural con Sol' ),
        (Som , 'Secado Natural en sombra'),
        (Gas , 'Secado a gas'),
    ]
    tipo_secado_cae_opciones = models.CharField(
        max_length=100,
        choices=tipo_secado_cae_choices, #Un grupo de valores de selección para este campo.
        default=Sol, #valor por defecto del campo
        null=True
    )

    #########################################################
    #                                                       #
    #              Modo de secado natural                   #
    #                                                       #
    #########################################################
    Lon = 'Lona'
    Mar = 'Marquesina' 
    Ban = 'Bandeja de secado'
    Ota = 'Otra'

    modo_secado_cae_choices = [
        (Lon , 'Lona'),
        (Mar , 'Marquesina' ),
        (Ban , 'Bandeja de secado'),
        (Ota , 'Otra'),
    ]
    modo_secado_cae_opciones = models.CharField(
        max_length=100,
        choices=modo_secado_choices, #Un grupo de valores de selección para este campo.
        default=Lon, #valor por defecto del campo
        null=True
    )

    #########################################################
    #                                                       #
    #     Tiempo de secado                                  #
    #                                                       #
    #########################################################    

    tiempo_cae_secado = models.CharField(
        max_length=20,
        null=True,
        help_text="Ingrese tiempo del proceso de secado: dias y horas para secado natural /horas para secado a gas",
        )
    
    #######################################################################
    #                                                                     #
    #       TRANSACCION DE VENTA A CENTRO DE ACOPIO DE LA EXPORTADORA     #
    #                                                                     #
    #######################################################################

    #######################################################################
    #                                                                     #
    #         PESAJE DEL LOTE TRANSFERIDO                                 #
    #                                                                     #
    #######################################################################

    peso_lote_cae=models.FloatField(
        null=True,
        default=0.00,
        help_text="Ingrese el peso EN LIBRAS del lote entregado por el productor/comerciante sin aplicar calificacion de humedad",
    )

    peso_lote_cae_calificado=models.FloatField(
        null=True,
        default=0.00,
        help_text="Ingrese el peso EN LIBRAS del lote entregado por el productor/comerciante CON ESTIMACION/CALIFICACION DE HUMEDAD",
    )

    #######################################################################
    #                                                                     #
    #         VALOR PAGADO POR QUINTAL                                    #
    #                                                                     #
    #######################################################################

    precio_lote_cae_qq=models.FloatField(
        null=True,
        default=0.00,
        help_text="Ingrese el PRECIO PAGADO  por QUINTAL",
    )

    #**********************************************************************************************************************************************************
    #**********************************************************************************************************************************************************
    #**********************************************************************************************************************************************************
    #
    #                                   CAMPOS DE LA EXPORTADORA
    #
    #**********************************************************************************************************************************************************
    #**********************************************************************************************************************************************************
    #**********************************************************************************************************************************************************
    
    ###################################################################
    #                                                                 #
    #                        NUMERO DE CONTRATO                       #
    #                                                                 #
    ###################################################################
    contrato_exp = models.CharField(
    max_length=15,
    null=True,
    help_text="Ingrese numero de contrato de exportacion",
    )

    ###################################################################
    #                                                                 # 
    #                       FACTURA                                   #
    #                                                                 #
    ###################################################################

    factura_exp = models.CharField(
    max_length=17,
    null=True,
    help_text="Ingrese numero de factura de exportación",
    )

    ###################################################################
    #                                                                 # 
    #                LOTE DE EXPORTACION                              #
    #                                                                 #
    ###################################################################

    lote_exp = models.CharField(
    max_length=20,
    null=True,
    help_text="Ingrese tiempo de fermentacion en dias y horas",
    )


    ###################################################################
    #                                                                 # 
    #                NUMERO DE CONTENEDORES                           #
    #                                                                 #
    ###################################################################

    numero_contenedores_exp=models.FloatField(
        null=True,
        default=0.00,
        help_text="Ingrese el número de contenedores (enteros o decimales)",
    )


    ###################################################################
    #                                                                 # 
    #                NUMERO DE SACOS                                  #
    #                                                                 #
    ###################################################################

    numero_sacos_exp=models.FloatField(
        null=True,
        default=0.00,
        help_text="Ingrese el número de sacos de 150 libras o 68 Kgs. (enteros o decimales)",
    )


    ###################################################################
    #                                                                 # 
    #                 TOTAL KILOGRAMOS BRUTOS                         #
    #                                                                 #
    ###################################################################

    total_kgs_b_exp=models.FloatField(
    null=True,
    default=0.00,
    help_text="Ingrese el número total de kilogramos brutos comercializados",
    )


    ###################################################################
    #                                                                 # 
    #                   TOTAL KILOGRAMOS NETOS                        #
    #                                                                 #
    ###################################################################

    total_kgs_n_exp=models.FloatField(
    null=True,
    default=0.00,
    help_text="Ingrese el número total de kilogramos netos comercializados",
    )

    ###################################################################
    #                                                                 # 
    #                       FECHA DE EMBARQUE                         #
    #                                                                 #
    ###################################################################

    fecha_embarque_exp = models.DateField(null=True, blank=True)


    ###################################################################
    #                                                                 # 
    #                            POSICION                             #
    #                                                                 #
    ###################################################################

    Mar = 'Marzo'
    Jul = 'Julio' 
    Sep = 'Septiembre'
    Dic = 'Diciembre'

    posiciones_exp_choices = [
        (Mar , 'Marzo'),
        (Jul , 'Julio'  ),
        (Sep , 'Septiembre'),
        (Dic , 'Diciembre'),
    ]
    posiciones_exp_opciones = models.CharField(
        max_length=100,
        choices=posiciones_exp_choices, #Un grupo de valores de selección para este campo.
        default=Dic, #valor por defecto del campo
        null=True
    )



    ###################################################################
    #                                                                 # 
    #                  PRECIO FOB POR TM                              #
    #                                                                 #
    ###################################################################

    precio_fob_tm_exp=models.FloatField(
    null=True,
    default=0.00,
    help_text="Ingrese el precio promedio negociado por TM",
    )


    ###################################################################
    #                                                                 # 
    #                           FRANQUICIA                            #
    #                                                                 #
    ###################################################################

    franquicia_exp=models.FloatField(
    null=True,
    default=0.00,
    help_text="Ingrese en decimales (2 decimales) el porcentaje de franquicia",
    validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
    )


    ###################################################################
    #                                                                 # 
    #                           CLIENTE                               #
    #                                                                 #
    ###################################################################

    cliente_exp = models.CharField(
    max_length=50,
    null=True,
    help_text="Ingrese nombre del cliente",
    )

    ###################################################################
    #                                                                 # 
    #                FECHA DE SALIDA DEL EMBARQUE                     #
    #                                                                 #
    ###################################################################    

    fecha_sal_emb_exp = models.DateField(null=True, blank=True)


    ###################################################################
    #                                                                 # 
    #                FECHA DE ARRIBO DEL EMBARQUE                     #
    #                                                                 #
    ###################################################################

    fecha_arr_emb_exp = models.DateField(null=True, blank=True)


    def  __str__(self):
        return '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (
            self.centro_acopio_opciones,
            self.cedula_productor, 
            self.cedula_vendedor,
            self.certificacion_opciones,
            self.Tipo_certificacion_opciones,
            self.Tipo_cacao_opciones,
            self.Tipo_especialidad_opciones,
            self.estado_cacao_opciones,
            self.fecha_compra_venta,
            self.fecha_inicio_cosecha,
            self.fecha_fin_cosecha,
            self.fermentacion_lote,
            self.tipo_fermentacion_opciones,
            self.tiempo_fermentacion,
            self.tipo_secado_opciones,
            self.modo_secado_opciones,
            self.tiempo_secado,
            self.tipo_transporte_opciones,
            self.peso_lote,
            self.peso_lote_calificado,
            self.precio_lote_qq,
            self.secado_en_cac_opciones,
            self.tipo_secado_cac_opciones,
            self.modo_secado_cac_opciones,
            self.tiempo_secado_cac,
            self.tipo_transporte_cac_opciones,
            self.transportista_cac,
        #   CAE 27
            self.fermentacion_cae_lote,
            self.tipo_fermentacion_cae_opciones,
            self.tiempo_cae_fermentacion,
            self.tipo_secado_cae_opciones,
            self.modo_secado_cae_opciones,
            self.tiempo_cae_secado,
        #exportadora 33
            self.contrato_exp,
            self.factura_exp,
            self.lote_exp,
            self.numero_contenedores_exp,
            self.numero_sacos_exp,
            self.total_kgs_b_exp,
            self.total_kgs_n_exp,
            self.fecha_embarque_exp,
            self.posiciones_exp_opciones,
            self.precio_fob_tm_exp,
            self.franquicia_exp,
            self.cliente_exp,
            self.fecha_sal_emb_exp,
            self.fecha_arr_emb_exp,
        #47    



            )
    class Meta:
        verbose_name = "Centros de acopio comunitario"

"""
###################################################################
#                                                                 # 
#     Lote  registrado en centro de acopio exportador             #
#                                                                 #
###################################################################

class cae_form(models.Model):
    lote_cae=models.CharField(
        help_text='Lote CAE', 
        max_length=30
        )
    centro_acopio_cae = models.CharField(
        help_text='Ingrese Centro de acopio exportadora', 
        max_length=30
        )
    usuario = models.CharField(
        help_text='Ingrese su usuario',
        max_length=30
        )
    exportadora = models.CharField(
        help_text='Ingrese Exportadora',
        max_length=30
        )
    def  __str__(self):
        return '%s' '%s' '%s' '%s'% (
            self.lote_cae,
            self.centro_acopio_cae,
            self.usuario,
            self.exportadora,
            )
    class Meta:
        verbose_name = "Centros de acopio exportadora" """
