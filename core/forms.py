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
