from django.contrib import admin
from .models import Conductor, Operador, LugaresDeTrabajo, Propinas, Denuncia, TipoDenuncia

admin.site.register(Conductor)
admin.site.register(Operador)
admin.site.register(LugaresDeTrabajo)
admin.site.register(Propinas)
admin.site.register(Denuncia)
admin.site.register(TipoDenuncia)
# Register your models here.

