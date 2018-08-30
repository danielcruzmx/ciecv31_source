import csv
from django.http import HttpResponse
from django.contrib import admin
from import_export import resources

# Register your models here.

from main.models import TipoMovimiento, Situacion, CuentaContable, \
                        Banco, Condominio, Proveedore, \
                        Periodo, TipoDocumento, Cuota, Menu
class ExportCsvMixin:

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Descarga movimientos seleccionados"

class TipoMovimientoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class SituacionAdmin(admin.ModelAdmin):
    list_display = ('situacion',)

class CuentaContableAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('num_cuenta', 'descripcion')
    list_filter = ('num_cuenta',)
    actions = ['export_as_csv']

class BancoAdmin(admin.ModelAdmin):
    list_display = ('clave','descripcion')

class CondominioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class ProveedoreAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'rfc', 'domicilio')

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('condominio', 'fecha_inicial', 'fecha_final')

class CuotaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'tipo_movimiento', 'descripcion', 'monto', 'cuenta_contable')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'link', 'nombre')

class CondominioResource(resources.ModelResource):

    class Meta:
        model = Condominio

admin.site.register(Menu, MenuAdmin)
admin.site.register(Cuota, CuotaAdmin)
admin.site.register(TipoMovimiento, TipoMovimientoAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(Situacion, SituacionAdmin)
admin.site.register(CuentaContable, CuentaContableAdmin)
admin.site.register(Banco, BancoAdmin)
admin.site.register(Condominio, CondominioAdmin)
admin.site.register(Proveedore, ProveedoreAdmin)
admin.site.register(Periodo, PeriodoAdmin)
