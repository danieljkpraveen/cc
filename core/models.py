from django.db import models
from cryptography.fernet import Fernet


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


class FirewallCredential(models.Model):
    """
    Model to store firewall connection credentials.
    """
    host = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    api_key = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.key = Fernet.generate_key().decode()
        cipher_suite = Fernet(self.key.encode())
        cipher_text = cipher_suite.encrypt(self.password.encode())
        self.password = cipher_text.decode()

        super().save(*args, **kwargs)

    def decrypt_password(self):
        cipher_suite = Fernet(self.key.encode())
        plain_text = cipher_suite.decrypt(self.password.encode())
        return plain_text.decode()

    def __str__(self):
        return self.host
