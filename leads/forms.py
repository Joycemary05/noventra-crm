from django import forms
from .models import Lead
from django.contrib.auth.models import User


class LeadForm(forms.ModelForm):

    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        empty_label="Select User"
    )


    class Meta:

        model = Lead

        fields = [
            "name",
            "email",
            "phone",
            "company",
            "source",
            "status",
            "message",
            "assigned_to",
        ]