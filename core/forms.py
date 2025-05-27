from django import forms
from .models import UploadExcelModel, UploadEMLModel


class UploadExcelForm(forms.ModelForm):
    """
    Form for uploading Excel files.
    """
    class Meta:
        model = UploadExcelModel
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'accept': '.xlsx, .xls'}),
        }


class UploadEMLForm(forms.ModelForm):
    """
    Form for uploading EML files.
    """
    class Meta:
        model = UploadEMLModel
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'accept': '.eml'}),
        }


class FirewallConnectForm(forms.Form):
    host = forms.CharField(label="Firewall Host/IP", required=True)
    username = forms.CharField(label="Username", required=True)
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput, required=False)
    api_key = forms.CharField(label="API Key", required=False)


class VersionSelectForm(forms.Form):
    version = forms.ChoiceField(label="PAN-OS Version", choices=[])


class ConfigUploadForm(forms.Form):
    config_file = forms.FileField(label="Upload XML Config")
    config_file.widget.attrs.update({'accept': '.xml'})
