
from    django.http                     import HttpResponseRedirect
from    django.http                     import HttpResponse
from    django.shortcuts                import render
from    django.shortcuts                import get_object_or_404
from    Registro.models                 import Registros_traz
from    Registro.forms                  import ContactForm,nombreform ,cae_modelform
from    django.core.mail                import send_mail
from    django.views.generic            import ListView
from    django_tables2.config           import RequestConfig
from    django_tables2.export.export    import TableExport
from    Registro.tables                 import Registros_traz_Table
import  datetime 

#####################################################################################################################################
#                                                                                                                                   #             
#                                   funcion para devolver la pagina de INICIO                                                       #
#                                                                                                                                   #                 
#####################################################################################################################################

def home(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"inicio.html", {"fecha_actual": fecha_actual})


#####################################################################################################################################
#                                                                                                                                   #             
#                                   funcion para devolver la pagina de INICIO BOOTSTRAP                                             #
#                                                                                                                                   #                 
#####################################################################################################################################

def home1(request):
    return render(request,"home.html")


############################################################################################################################################
#                                                                                                                                          #             
# vista/funcion para trabajar con el modelo Registros_traz  ---> FORMULARIO DE REGISTRO WEB DE INFORMACION --> REGISTRO DE INFORMACION     #
#                                                                                                                                          #                 
############################################################################################################################################

def add(request):
    fecha_actual=datetime.datetime.now()
    # Creamos un formulario vacío
    form5 = cae_modelform()
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form5 = cae_modelform(request.POST)
        # Si el formulario es válido...
        if form5.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form5.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            # Después de guardar redireccionamos a la lista
            return HttpResponseRedirect('/gracias/')
    # Si llegamos al final renderizamos el formulario
    return render(request, "form_cae.html", {'form5': form5,"fecha_actual": fecha_actual})

#############################################################################################################################
#                                                                                                                           #             
#   funcion para devolver la pagina de filtrado de clientes, lotes y contratos renderizada  ---> TRAZABILIDAD CLIENTE       #
#                                                                                                                           #                 
#############################################################################################################################

def filtrar(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"filtrar.html", {"fecha_actual": fecha_actual})


####################################################################################################################################
#                                                                                                                                  #             
#               Funcion para devolver resultados del FILTRO CLIENTE LOTE CONTRATO --> TRAZABILIDAD CLIENTE                         #
#                                                                                                                                  #                 
####################################################################################################################################

def customer_search(request):
    if  request.GET["cust"] and request.GET["lote_id"] and request.GET["contract_id"]:
        cliente   =   request.GET["cust"]
        lote      =   request.GET["lote_id"]
        contrato  =   request.GET["contract_id"]
        if  len(cliente)<50 and len(lote)<20 and len (contrato)<20:
            product=Registros_traz.objects.filter(cliente_exp__icontains=cliente)
            product1= product.filter(lote_exp__icontains=lote)
            product2= product1.filter(contrato_exp__icontains=contrato)
            #icontains es equivalente a like en lenguaje sql
            #desde aca empiezo a trabajar en una tabla
            table=Registros_traz_Table(Registros_traz.objects.filter(cliente_exp__icontains=cliente,lote_exp__icontains=lote))                             #product2 es un query set, perfecto pero me parece que le falta parametros
            RequestConfig(request).configure(table) #necesito para paginar y para exportar
            export_format = request.GET.get("_export", None)
            if  TableExport.is_valid_format(export_format):
                exporter = TableExport(export_format, table)
                return exporter.response("table.{}".format(export_format))
            table.paginate(page=request.GET.get("page", 1), per_page=10)
            return render (request,"resultados_productores_table.html",{"Productores":product2,"query":cliente, "query1":lote,"query2":contrato,"table": table})
        else:
            mensaje="No existen registros o cadena de busqueda demasiado larga"
    else:

        mensaje="No se ha ingresado adecuadamente cliente, lote de exportación y contrato de exportacion"
    return HttpResponse(mensaje)


##########################################################################################################################
#                                                                                                                        #             
#   funcion para devolver la pagina buscador por cedula y fecha de venta renderizada ---> REPORTES TRANSACCIONALES       #
#                                                                                                                        #                 
##########################################################################################################################

def buscador(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"buscador.html", {"fecha_actual": fecha_actual})

####################################################################################################################################
#                                                                                                                                  #             
#   funcion para devolver resultados del filtro de busqueda a la bbdd del modelo Registros_Traz --> REPORTES TRANSACCIONALES       #
#                                                                                                                                  #                 
####################################################################################################################################

def resultados(request):
    if  request.GET["cc"] and request.GET["fcv"]:
        #mensaje= "Articulo buscado %r" %request.GET["prd"]
        #en una variable llamada producto almaceno prd que contiene
        #el valor que se ingresa en el cuadro de texto de busqueda
        productor   =   request.GET["cc"]
        fecha_cv    =   request.GET["fcv"]   
        if  len(productor)<20:
            productores=Registros_traz.objects.filter(cedula_productor__icontains=productor)
            productores1= productores.filter(fecha_compra_venta__icontains=fecha_cv)
            #icontains es equivalente a like en lenguaje sql
            return render (request,"resultados.html",{"productores":productores1,"query":productor, "query1":fecha_cv})
        else:
            mensaje="Cadena de busqueda demasiado larga"
    else:

        mensaje="No se ha ingresado ningún productor para la búsqueda"
    return HttpResponse(mensaje)

####################################################################################################################################
#                                                                                                                                  #             
#                               vista/funcion retornar un formulario de contacto con envío de correo  -->  CONTACTO                #
#                                                                                                                                  #                 
####################################################################################################################################

def contact(request):
    fecha_actual=datetime.datetime.now()
    if request.method == 'POST':
        form1 = ContactForm(request.POST)
        if form1.is_valid():
            asunto = form1.cleaned_data['asunto']
            mensaje = form1.cleaned_data['mensaje']
            remitente = form1.cleaned_data['remitente']
            copia_a_mi = form1.cleaned_data['copia_a_mi']
            receptor = ['daalroar@gmail.com'] #este correo es el receptor universal del formulario de contactos una cuenta tipo info_trazabilidad@corporacionintelnaes.com.ec
            if copia_a_mi:
                receptor.append(remitente)
            send_mail(asunto, mensaje, remitente, receptor)
            return HttpResponseRedirect('/gracias/')
    else:
        form1 = ContactForm()
    return render(request, 'contacto.html', {'form1': form1,"fecha_actual": fecha_actual })


####################################################################################################################################
#                                                                                                                                  #             
#                               vista/funcion para devolver la hoja de agradecimiento                                              #
#                                                                                                                                  #
####################################################################################################################################

def gracias(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"gracias.html", {"fecha_actual": fecha_actual})
