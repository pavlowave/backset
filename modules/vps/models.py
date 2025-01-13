from django.db import models

class VPS(models.Model):
    STATUS_CHOICES = [
        ('started', 'Started'),
        ('blocked', 'Blocked'),
        ('stopped', 'Stopped'),
    ]

    uid = models.CharField(max_length=36, unique=True)
    cpu = models.PositiveIntegerField()
    ram = models.PositiveIntegerField()
    hdd = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='stopped')

    def __str__(self):
        return f"VPS {self.uid}"
