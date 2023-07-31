from django import forms
from authors import models


class AuthorsForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = "__all__"
