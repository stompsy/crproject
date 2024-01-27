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
