from django.db import models

# Create your models here.


class Skill(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    description = models.TextField(blank=True, verbose_name="Description")
    image = models.ImageField(upload_to='Skills/', blank=True, null=True)

    def __str__(self):
        return self.title


class Parcour(models.Model):
    STATUS_CHOICES = [
        ('cdi', 'CDI'),
        ('cdd', 'CDD'),
        ('stage', 'STAGE'),
        ('formation', 'FORMATION'),
    ]
    title = models.CharField(max_length=255, verbose_name="Titre")
    debut = models.DateField(blank=True, null=True)
    fin = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, verbose_name="Description", null=True)
    logo = models.ImageField(upload_to='Parcours/',blank=True, null=True)
    entreprise = models.CharField(max_length=255, verbose_name="entreprise", null=True)
    ville = models.CharField(max_length=255, verbose_name="Ville", null=True)
    pays = models.CharField(max_length=255, verbose_name="Pays", null=True)
    type = models.CharField(max_length=40, choices=STATUS_CHOICES, default='', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
