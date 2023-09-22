from django.db import models
from django.contrib.auth.models import User

class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    ROLE_CHOICES = [ 
        ('Psicólogo', 'Psicólogo'),
        ('Aprendiz', 'Aprendiz')
        ]

    role = models.CharField(choices = ROLE_CHOICES, max_length = 15, null=True, blank=True, verbose_name= 'rol')

    def __str__(self):
        return self.user
    


class Missions(models.Model):
    name = models.CharField(max_length=250, verbose_name = 'Nombre Mision')
    numberMission = models.PositiveIntegerField(verbose_name = 'Numero Misiones')
    objetive = models.CharField(max_length=250, verbose_name = 'Objetivo Mision')
    typeMission = models.CharField(max_length=250, verbose_name= 'Tipo Mision')
    result = models.CharField(max_length=250, verbose_name = 'Resultado Mision')

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Misiones"
        db_table = "Misiones"
        ordering = ["id"]

class PersonalizedAdvice(models.Model):
    typeAdvice = models.CharField(max_length=250, verbose_name= 'Tipo Asesoria')
    topic = models.CharField(max_length= 250, verbose_name= 'Tema Asesoria')
    suggestion = models.TextField(max_length= 250, verbose_name= 'Sugerencias')
    historialAdvice = models.CharField(max_length= 250, verbose_name= 'Historial Asesorias')
    missions = models.ManyToManyField(Missions, verbose_name= 'Asesoramiento Misión')

    def __str__(self):
        return self.typeAdvice
    
    class Meta:
        verbose_name = "Asesoria"
        verbose_name_plural = "Asesorias"
        db_table = "Asesorias"
        ordering = ['id']

class ForumInformation(models.Model):
    comment = models.TextField(max_length = 1000, verbose_name= 'Comentarios')
    calification = models.IntegerField(default=0, verbose_name="Calificacion")

    def __str__(self):
        return self.comment
    
    class Meta:
        verbose_name = "Comentarios"
        db_table = "Comentarios"
        ordering = ['id']