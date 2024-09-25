from django.forms import ModelForm
from .models import ExpLists

class Test1Form(ModelForm):
    class Meta:
        model = ExpLists
        fields = '__all__'


