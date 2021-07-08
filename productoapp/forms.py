from django import forms
from .models import Producto

class FormProducto(forms.ModelForm):

    #campos del modelo
    class Meta:
        model = Producto
        fields = '__all__'
        # widgets = {
        #     'fecha_publicacion': forms.SelectDateWidget(attrs={'class': 'pub_fecha_publicacion'}),
        #     'titulo': forms.TextInput(attrs={'class': 'pub_titulo'}),
        #     'contenido': forms.Textarea(attrs={'class': 'pub_contenido'}),
        #     'imagen': forms.FileInput(attrs={'name':'imagen_adjunta', 'class': 'pub_imagen'}),
        # }