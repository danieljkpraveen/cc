from django import forms


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
