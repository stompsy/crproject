from django import forms
from .models import Agency


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = [
            "agency_name",
            "agency_url",
            "agency_description",
        ]

    def clean(self):
        data = self.cleaned_data
        agency_name = data.get("agency_name")
        qs = Agency.objects.filter(agency_name__icontains=agency_name)
        if qs.exists():
            self.add_error("agency_name", f"{agency_name} is already in use.")
        return data


class AgencyFormOld(forms.Form):
    agency_name = forms.CharField()
    agency_url = forms.URLField()
    agency_description = forms.CharField(widget=forms.Textarea)


# def clean_agency_name(self):
#     cleaned_data = self.cleaned_data
#     agency_name = cleaned_data.get("agency_name")
#     if agency_name.lower().strip() == "Hello":
#         raise forms.ValidationError("This title is taken.")
#     return agency_name


def clean(self):
    cleaned_data = self.cleaned_data
    agency_name = cleaned_data.get("agency_name")
    agency_url = cleaned_data.get("agency_url")
    agency_description = cleaned_data.get("agency_description")
    if agency_name.lower().strip() == "Hello":
        raise forms.ValidationError("This title is taken.")

    return cleaned_data
