from django import forms

from home.models import Myprofile


class MyprofileForm(forms.ModelForm):

    def clean_EMP_ID(self):
        emp_id = self.cleaned_data['EMP_ID']
        if not emp_id:
            raise forms.ValidationError("Employee I'd can not be emtpy")
        return emp_id
    class Meta:
        model = Myprofile
        fields = "__all__"
