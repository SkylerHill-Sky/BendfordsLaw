from django.forms import ModelForm
from main.models import TextFile


class TextFileForm(ModelForm):
    class Meta:
        model = TextFile
        fields = ['file', 'file_name']