from django.contrib import admin
from django.urls import path,include
from tiendaApp import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.principal, name='principal'),
    path('inicio/',v.inicio,name='inicio'),
    path('infotenis/',v.infotenis,name='infotenis'),
    path('infoft/',v.infoft,name='infoft'),
    path('infopadel/',v.infopadel,name='infopadel'),
    path('horario/', v.horario_semanal, name='horario_semanal'),
    path('empleado/',v.crear_empleado,name="empleado"),
    path('empleados/',v.mostrar_empleados,name="empleados"),
    path('empleadoEdit/<int:empleado_id>/',v.cargar_editar_empleado,name='editarEmpleado'),
    path('empleadoEditado/<int:empleado_id>/',v.editar_empleado,name='empleadoEditado'),
    path('empleadoDel/<int:empleado_id>/',v.eliminar_empleado,name='empleadoDel'),
    path('cliente/',v.crear_cliente,name="cliente"),
    path('clientes/',v.mostrar_clientes,name="clientes"),
    path('clienteEdit/<int:cliente_id>/',v.cargar_editar_cliente,name='editarCliente'),
    path('clienteEditado/<int:cliente_id>/',v.editar_cliente,name='clienteEditado'),
    path('clienteDel/<int:cliente_id>/',v.eliminar_cliente,name='clienteDel'),
    path('canchas/nueva/', v.crear_cancha, name='crear_cancha'),
    path('canchas/<str:tipo>/', v.listar_canchas, name='listar_canchas_tipo'),
    path('listar_canchas/', v.listar_canchas, name='listar_canchas_general'),
    path('canchaEdit/<int:cancha_id>/', v.cargar_editar_cancha,name='editarCancha'),
    path('canchaEditada/<int:cancha_id>/',v.editar_cancha, name='canchaEditada'),
    path('canchaDel/<int:cancha_id>/',v.eliminar_cancha,name='canchaDel'),
    path('reserva/',v.crear_reserva,name="reserva"),
    path('reservas/',v.mostrar_reservas,name="reservas"),
    path('reservaEdit/<int:reserva_id>/',v.cargar_editar_reserva,name='editarReserva'),
    path('reservaEditado/<int:reserva_id>/',v.editar_reserva,name='reservaEditado'),
    path('reservaDel/<int:reserva_id>/',v.eliminar_reserva,name='reservaDel'),
    path('account/',include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
