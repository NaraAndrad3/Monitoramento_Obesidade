from django.db import models
from uuid import uuid4

# aqui crio os modelos (as tabelas)
# modifiquei a tabela para que ela tenha os atributos da base de dados
class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True, editable=False)
    genero = models.IntegerField(default=0)
    idade = models.IntegerField(default=0)
    altura = models.FloatField(default=0)
    peso = models.FloatField(default=0)
    family_history = models.IntegerField(default=0) # 1-sim ou 0-não
    FAVC = models.IntegerField(default=0) # sim ou não
    FCVC = models.IntegerField(default=0) # 1 - Nunca, 2 - As vezes, 3 - Sempre
    NCP = models.IntegerField(default=0)
    CAEC = models.IntegerField(default=0) # ver as possibilidades de resposta na base de dados
    SMOKE = models.IntegerField(default=0) # 0 - não 1 - sim
    CH2O = models.FloatField(default=0) # 1 - lass then a liter 2 - between 1 and 2L 3 - more than 2L
    SCC = models.IntegerField(default=0) # 1 - sim ou 0 - não
    FAF = models.FloatField(default=0) # 0 - não pratuca 1 - 1 ou 2 dias 2- 2 ou 4 dias 3-  4 ou 5 dias
    TUE = models.FloatField(default=0) # 0 - 0 a 2 hrs, 1 - 3 a 5 horas, 2 - mais de 5hrs
    CALC = models.IntegerField(default=0) # 0 - sempre, 1 - com frequencia, 2 - as vezes, 3 - nao bebe
    MTrans = models.IntegerField(default=0) # 0 - automovel, 1 - bicicleta, 2 - moto, 3 - transporte publico, 4 - a pé
    NObeyesdad = models.IntegerField(default=-1)

