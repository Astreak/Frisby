from django.forms import ModelForm
from .models import *
class CarForm(ModelForm):
    class Meta:
        model=car
        fields=["Owner","name","price","color","date"]

class MsgForm(ModelForm):
    class Meta:
        model=Msg
        fields=["sen","rec","text","HOLDER"]

class CreateUser(ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]

class MusicForm(ModelForm):
    class Meta:
        model=Music
        fields=["genre","subscriber","song","urls"]

class MedicalForm(ModelForm):
    class Meta:
        model=Medical
        fields=["name","age","img","diagnosis"]
