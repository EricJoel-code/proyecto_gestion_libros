from django.forms import ModelForm
from .models import Libros

class BookForm(ModelForm):
    class Meta:
        model = Libros
        fields = ['title','description','image']