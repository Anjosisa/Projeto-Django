from django import forms

TIPOS_QUARTOS = (
    ("SOLTEIRO", "Solteiro"),
    ("CASAL", "Casal"),
    ("CONFORTO","Conforto"),
    ("LUXO","Luxo")
)

class FormNome(forms.Form):
    nome = forms.CharField(label= 'Nome', max_length= 20)
    sobrenome = forms.CharField(label= 'Sobrenome', max_length= 20)
    email = forms.CharField(label= 'Email', max_length= 50)
    idade = forms.CharField(label= 'Idade', max_length= 3)
    endereco = forms.CharField(label= 'Endereço', max_length= 50)
    quarto = forms.ChoiceField(label= 'Quarto', choices=TIPOS_QUARTOS)
    data = forms.DateField(label='Data', widget=forms.DateInput(attrs={'type': 'date'}))