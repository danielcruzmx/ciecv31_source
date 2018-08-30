from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from main import views
from rest_framework import routers

#from welcome.views import index, health
admin.site.site_header = "Cuotas, Ingresos y Egresos Condominales"
admin.site.site_title = "CIEC Admin Portal"
admin.site.index_title = "Bienvenido al Admin CIEC"

router = routers.DefaultRouter()
router.register(r'menu', views.MenuViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api-rest/olimpo/informe/(?P<depto_id>[\w]+)/$',
    views.CuotasViewSet.as_view(), name='my_rest_view'),
    url(r'^api-rest/totalIngresosEgresos/(?P<condominio>[\w]+)/(?P<fec_ini>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/(?P<fec_fin>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/$',
    views.TotalIngresosEgresosViewSet.as_view(), name='my_rest_view'),
    url(r'^api-rest/cuotasDeptoMes/(?P<condominio>[\w]+)/(?P<mes_anio>(0?[1-9]|1[012])-((19|20)\d\d))/$',
    views.CuotasDeptoMesViewSet.as_view(), name='my_rest_view'),
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^explorer/', include('explorer.urls')),
    url(r'^catalogos/', include(router.urls)),
]

'''if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
'''
