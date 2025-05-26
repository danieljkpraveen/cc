from django.contrib import admin
from .models import UploadExcelModel, UploadEMLModel


admin.site.register(UploadExcelModel)
admin.site.register(UploadEMLModel)
