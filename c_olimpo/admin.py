from django.contrib import admin
from django.forms.models import model_to_dict
#from django.contrib.filters import RelatedOnlyFieldListFilter

# Register your models here.

from c_olimpo.models import Condomino, Estacionamiento, CuentaBanco, \
                            DetalleMovimiento, Documento, Movimiento, Asiento

from main.models	import CuentaContable
from main.admin     import ExportCsvMixin

class DetalleMovtoInline(admin.TabularInline):
	model = DetalleMovimiento
	fields = ['cuenta_contable', 'monto', 'proveedor']
	#list_display = ('cuenta_contable',)

	def get_extra(self, request, obj=None, **kwargs):
		extra = 4
		#if(obj):
		#	return extra - DetalleMovimiento.objects.filter(id = request.id).count()
		return extra

	#def cuenta_contabledos(self, request, obj=None, **kwargs):
	#   return	CuentaContable.objects.filter(clave_mayor = '41')

class MovtoAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('id','fecha','concepto','retiro','deposito','condomino','detalle','conciliacion')
    list_filter = ('fecha','condomino',)
    date_hierarchy = 'fecha'
    readonly_fields = ('detalle',)
    ordering = ('-fecha',)
    save_on_top = True
    inlines = [DetalleMovtoInline]
    actions = ['export_as_csv']

    def concepto(self, request, obj=None, **kwargs):
        return '%s %s' % (request.tipo_movimiento,request.descripcion)

    def detalle(self, request, obj=None, **kwargs):
        cantidades =  DetalleMovimiento.objects.filter(movimiento_id = request.id).values_list('monto', flat = True)
        total = sum(cantidades)
        return total

    def conciliacion(self, request, obj=None, **kwargs):
        cantidades =  DetalleMovimiento.objects.filter(movimiento_id = request.id).values_list('monto', flat = True)
        total = sum(cantidades)
        if(total != (request.retiro + request.deposito)):
            return False
        else:
            return True

    conciliacion.boolean = True

class CuentaBancoAdmin(admin.ModelAdmin):
    list_display = ('banco','clabe','apoderado')

class CondominoAdmin(admin.ModelAdmin):
	list_display = ('depto','propietario','cargos','depositos','cuotas')
	search_fields = ('depto','propietario','poseedor')

class EstacionamientoAdmin(admin.ModelAdmin):
	list_display = ('ubicacion',)

class DocumentoAdmin(admin.ModelAdmin):
	list_display = ('tipo_documento','folio','fecha_expedicion','monto_total')

class AuxiliarAdminA(admin.ModelAdmin):
	list_display = ('id','fecha','tipo_movimiento','debe','haber','descripcion', 'cuenta_contable','condomino')
	list_filter = ('fecha', 'condomino',)
	date_hierarchy = 'fecha'
	ordering = ('-fecha',)

class DetalleMovimientoAdminA(admin.ModelAdmin):
    list_display = ('fecha', 'condomino', 'cuenta_contable', 'monto')
    list_filter = ('cuenta_contable',)
    ordering = ('movimiento',)

    def fecha(self, request, obj=None, **kwargs):
        fechamov = Movimiento.objects.filter(id = request.movimiento_id).values_list('fecha', flat = True)
        return fechamov[0]

    def condomino(self, request, obj=None, **kwargs):
        id_condom = Movimiento.objects.filter(id = request.movimiento_id).values_list('condomino_id', flat = True )
        condom = Condomino.objects.filter(id = sum(id_condom)).values_list('depto', flat = True)
        return condom[0]

admin.site.register(Movimiento, MovtoAdmin)
admin.site.register(CuentaBanco, CuentaBancoAdmin)
admin.site.register(Condomino, CondominoAdmin)
admin.site.register(Estacionamiento, EstacionamientoAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Asiento, AuxiliarAdminA)
admin.site.register(DetalleMovimiento, DetalleMovimientoAdminA)
