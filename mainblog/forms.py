from django import forms

class ProyectoFormulario(forms.Form):
    project_name = forms.CharField()
    investigation_area = forms.CharField()
    images = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea())


class AutorForm(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()
    country = forms.CharField()


class PublishingCompanyForm(forms.Form):
    publishing_name = forms.CharField()
    location = forms.CharField()
    publication_date = forms.DateField()