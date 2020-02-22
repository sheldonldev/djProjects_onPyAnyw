from django.forms import ModelForm

from .models import MakeUser


class MakeForm(ModelForm):
    class Meta:
        model = MakeUser
        fields = '__all__'
