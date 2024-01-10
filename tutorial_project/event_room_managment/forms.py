from django import forms

from .models import Room

# la classe qui va permettre de selctionner plusieurs fichiers silmultanement
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

# le classe qui initialise le champ et validera les fichiers qui seront uploader avec la methode clean
class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
    
# on cree le formulaire qui pa permettre la creation d'une sale
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room # le model qui va permettre de creer des instance du formualire
        fields = ['typ', 'daily_rate', 'city', 'neighborhood', 'description', 'images'] # les champs qui seront present dans le formulaire

    choices = [
    ('mariage', 'Mariage'),
    ('anniversaire', 'Anniversaire'),
    ('conference', 'Conference'),
    ('reunion', 'Reunion'),
    ('ceremonie', 'Ceremonie'),
    ]
    typ = forms.ChoiceField(choices=choices, label='type') # je change le label de ce champ en type
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}), help_text='champ facultatif', required=False)
    images = MultipleFileField(required=True)
    

    


