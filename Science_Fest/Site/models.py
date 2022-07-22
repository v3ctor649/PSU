from django.db import models

# Create your models here.

class Concurs(models.Model):
    header = models.CharField(verbose_name="Название фестиваля",null=False,blank=False,max_length=255)
    description = models.TextField(verbose_name="Описание фестиваля",null=False,blank=False)
    data = models.DateField("Дата проведения",null=False,blank=False)


    class Meta:
        verbose_name = "Фестиваль"
        verbose_name_plural = "Фестивали"
        ordering = ['-id']
    def __str__(self):
        return self.header

class Participant(models.Model):
    fest_id = models.ForeignKey(Concurs,verbose_name="Название фестиваля",on_delete=models.CASCADE)
    surname = models.CharField(verbose_name="Фамилия",null=False,blank=False,max_length=30)
    name = models.CharField(verbose_name="Имя",null=False,blank=False,max_length=30)
    email = models.EmailField()
    
    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"
        ordering = ['-id']