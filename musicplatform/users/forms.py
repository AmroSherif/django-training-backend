from django import forms
from .models import ExtendedUser


class ExtendedUserForm(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        widgets = {"bio": forms.Textarea}
        fields = "__all__"

    def save(self, commit=True):
        m = super(ExtendedUserForm, self).save(commit=False)
        m.set_password(m.password)
        if commit:
            m.save()
        return m
