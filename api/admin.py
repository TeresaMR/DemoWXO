from django.contrib import admin
from .models import Trabajadores
from .models import Vacaciones
from .models import Fechas_Importantes

admin.site.register(Trabajadores)
admin.site.register(Vacaciones)
admin.site.register(Fechas_Importantes)