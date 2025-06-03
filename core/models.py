from django.db import models
from cryptography.fernet import Fernet


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
        cipher_text_pass = cipher_suite.encrypt(self.password.encode())
        cipher_text_api = cipher_suite.encrypt(self.api_key.encode())
        self.password = cipher_text_pass.decode()
        self.api_key = cipher_text_api.decode()

        super().save(*args, **kwargs)

    def decrypt_password(self):
        cipher_suite = Fernet(self.key.encode())
        plain_text = cipher_suite.decrypt(self.password.encode())
        return plain_text.decode()

    def decrypt_api_key(self):
        cipher_suite = Fernet(self.key.encode())
        plain_text = cipher_suite.decrypt(self.api_key.encode())
        return plain_text.decode()

    def __str__(self):
        return self.host
