from django.db import models

# Create your models here.





class Tribo(models.Model): 
	nome = models.CharField(max_length=150, unique=True) 
	telefone = models.CharField(max_length=30, null=True,blank=True,unique=True)
	email = models.EmailField(null=True,blank=True) 
	data = models.DateField(max_length=20, null=True) 
	localizacao = models.CharField(max_length=255, null=True, default="Sem Localização")
	descricao = models.TextField(max_length=3000, null=True, default="Sem Descrição") 
	#active =models.BooleanField(default=True)

	def __str__(self):
		return "{}". format(self.nome)  