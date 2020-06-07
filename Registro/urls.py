from django.urls            import path
from Registro               import views

#ojo no se trae admin, admin queda en el proyecto

urlpatterns = [
    path('inicio/', views.home),                                                # pagina de inicio
    path('registro/', views.add, name="registro"),                              # pagina donde se realiza el REGISTRO DE INFORMACION
    path('filtrar/', views.filtrar, name="filtrar"),                            # pagina donde se ingresa clientes, contrato, lote para busqueda para TRAZABILIDAD DE CLIENTES
    path('resultados_productores/', views.customer_search),                     # pagina donde presentan los resultados del filtrado de clientes, contrato, lote RESULTADOS DE TRAZABILIDAD PARA CLIENTES
    path('busqueda_productores/', views.buscador, name="busqueda_productores"), # pagina donde se ingresan criterios de busqueda de productores REPORTES TRANSACCIONALES
    path('resultados_transacciones/', views.resultados),                        # pagina donde se presentan resultados de busqueda de productores REPORTES TRANSACCIONALES
    path('contacto/', views.contact, name="contacto"),                                           # pagina dde contacto
    path('gracias/', views.gracias, name="gracias"),                                            # pagina de retorno despues de cargar mensaje a través de REGISTRO DE INFORMACION Y CONTACTOS
    path('home/', views.home1, name="home"),                                    # pagina de inicio alternativa

]