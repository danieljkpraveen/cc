from django.db import models


class UploadExcelModel(models.Model):
    """
    Model to store uploaded Excel files.
    """
    file = models.FileField(upload_to='uploads/excel/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Excel File: {self.file.name} uploaded at {self.uploaded_at}"


class UploadEMLModel(models.Model):
    """
    Model to store uploaded EML files.
    """
    file = models.FileField(upload_to='uploads/eml/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"EML File: {self.file.name} uploaded at {self.uploaded_at}"
