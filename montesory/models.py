
from django.contrib.auth.models import User

from django.db import models
from django.db.models.signals import *
# Create your models here.
from django.contrib.auth.models import User,AbstractBaseUser,AbstractUser

SEXE=(('Famme','famme'),('Homme','homme'),)
# Enseignat Model -----------------------------------------------------------------------
class Enseignant(models.Model) :
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    sexe =models.CharField(choices=SEXE,max_length=25)
    numero_telephone=models.CharField(max_length=255,blank=True,null=True)
    adr=models.CharField(max_length=255,blank=True,null=True)
    code_postale=models.IntegerField(null=True)
    def __str__(self):
        return self.user.first_name+","+self.user.last_name.swapcase()



# Parent Model -----------------------------------------------------------------------

class Parent(models.Model) :
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    adr=models.CharField(max_length=255,null=True,blank=True)
    numero_telephone=models.CharField(max_length=255,null=True,blank=True)
    sexe=models.CharField(choices=SEXE,max_length=25)
    adr_tr=models.CharField(max_length=255)
    def __str__(self):
        return self.user.first_name
# Groupe Model -----------------------------------------------------------------------

class Groupe(models.Model):
    designation = models.CharField(max_length=255)
    nb_enfant = models.IntegerField()
    nb_enfant_max = models.IntegerField()
    niveau = models.CharField(max_length=25)
    def __str__(self):
        return self.designation
# Module Model -----------------------------------------------------------------------

class Module(models.Model):
    designation=models.CharField(max_length=255)
    def __str__(self):
        return self.designation
# Enfant Model -----------------------------------------------------------------------

class Enfant(models.Model):
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE,null=True,blank=True)
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)
    sexe=models.CharField(choices=SEXE,max_length=25)
    date_de_naissance=models.DateField()
    groupe=models.ForeignKey(Groupe,on_delete=models.CASCADE)
    def __str__(self):
        return self.prenom+" "+self.nom

# REMARQUE ENSEIGNATN Model -----------------------------------------------------------------------




class RemarqueParent(models.Model):
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    enseignant=models.ForeignKey(Enseignant,on_delete=models.CASCADE)
    remarque=models.CharField(max_length=1000)
# Remarque Parent Model -----------------------------------------------------------------------

class RemarqueEnseignant(models.Model):
    enseignant=models.ForeignKey(Enseignant,on_delete=models.CASCADE)
    enfant=models.ForeignKey(Enfant,on_delete=models.CASCADE)
    remarque=models.CharField(max_length=1000)


# gestion d eseignanment Model -----------------------------------------------------------------------

class Enseignament(models.Model):
    enseignant =models.ForeignKey(Enseignant,on_delete=models.CASCADE)
    module=models.ForeignKey(Module,on_delete=models.CASCADE)
    groupe=models.ForeignKey(Groupe,on_delete=models.CASCADE)


    def __str__(self):
      return self.groupe.designation + " ---> " + self.module.designation+" ---> "+self.enseignant.__str__()



class Article(models.Model):
    titre=models.CharField(max_length=1000)
    discription=models.CharField(max_length=1000)
    pic=models.ImageField(default='default.jpg')




class MessageA(models.Model):
    mes=models.CharField(max_length=1000)
    is_visted=models.BooleanField(default=False)


class MessageB(models.Model):
    mes=models.CharField(max_length=2555)
    is_visted=models.BooleanField(default=False)

