from django import forms
from app.models import tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = tarea
        fields = ['titulo_tarea', 'descripcion_tarea', 'maestro', 'ciclo_grado_curso', 'nota_tarea', 'fecha_entrega', 'estado_tarea']
        labels = {'titulo_tarea':'Titulo', 'descripcion_tarea':'DescripcionT', 'maestro':'Maestro', 'ciclo_grado_curso':'CicloGC', 'nota_tarea':'Nota', 'fecha_entrega':'FEntrega', 'estado_tarea':'Estado'}
        widget = {'tarea', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
