from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import Permission ,Group
from django.utils.datastructures import MultiValueDictKeyError

from montesory.forms import *
from django.contrib.auth import views as auth_views, authenticate,get_user
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from django.contrib.auth import update_session_auth_hash

# Create your views here.
#----------------------------ALL VIEWS--------------------------------------------------
#----------------------------First Page-------------------------------------------

def first_page(request):
    return render(request, "montesory/admin/index.html")
#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

def valide(request):
    print(get_user(request).groups.get(pk=1))
    g=Group.objects.get(pk=1)
    g2=Group.objects.get(pk=2)
    print(g)
    if get_user(request).is_superuser :
        return redirect("")
    else:
        if get_user(request).groups.get(pk=1) == g:
         print("je suis la")
         return redirect("teacher",get_user(request).id)
        elif get_user(request).groups.get(pk=1) == g2 :
         return redirect("",get_user(request).id)

    return HttpResponse("coucou")


def ensei(request,id_user):
    print("ze3bola")
    if id_user==get_user(request).id:
     return render(request, "montesory/admin/ensei.html", {'user_id':id_user})
    else:
        return HttpResponse("you'r not loged in")

#----------------------------ADMIN VIEWS-------------------------------------------


#----------------------------Dashboard Admin-------------------------------------------


def dashboardAdmin(request):
    groupes=Groupe.objects.all()
    return render(request, "montesory/admin/dashboardAdmin.html", {'groupes':groupes, })
#-----------------------------------------------------------------------------------
#----------------------------Ajouter Enseignant-------------------------------------------

def ajouterEnseignant(request):
    g=Group()
    g=Group.objects.filter(name="Enseignant")
    error=""
    form=EnseignantForm(request.POST or None)
    envoi=False

    if form.is_valid():
        users=User.objects.all()
        first_name = form["first_name"].value()
        last_name =form["last_name"].value()
        email = form["email"].value()
        username =form["username"].value()
        password1 =form['password'].value()
        numero_telephone = form["numero_telephone"].value()
        sexe = form["sexe"].value()
        adr = form["adr"].value()
        code_postale = form["code_postal"].value()

        for i in users:
            if username == i.username:
                error="ce nom d'utlisateur exist deja"
        user,created =User.objects.get_or_create(first_name=first_name,last_name=last_name,email=email,username=username)
        if created:

                user.set_password(password1)
                for per in Permission.objects.all():
                    user.user_permissions.add(per.id)
                user.is_staff=True
                user.groups.add(1)
                user.save()
                Enseignant.objects.create(user=user,numero_telephone=numero_telephone,sexe=sexe,adr=adr,code_postale=code_postale)
        else:
            return HttpResponse("non deja exist")
        envoi=True
        return redirect("enseignants")




    return render(request, "montesory/admin/AjouterEnseignant.html", locals())

#-----------------------------------------------------------------------------------------------------------------------------

def ajouterGroupe(request):
    form2=ModifierGroupeForm(request.POST or None)

    if form2.is_valid():
        print("zekri")
        gr1=Groupe.objects.get(pk=form2['groupe1'].value())
        designation1 = form2['designation1'].value()
        nb_enfant_max1 = form2['nb_enfant_max1'].value()
        niveau1 = form2['niveau1'].value()
        gr1.niveau=niveau1
        gr1.designation=designation1
        gr1.nb_enfant_max=nb_enfant_max1
        gr1.save()
    form=groupeForm(request.POST or None)

    if form.is_valid():
        designation =form['designation'].value()
        nb_enfant_max = form['nb_enfant_max'].value()
        niveau= form['niveau'].value()
        Groupe.objects.create(designation=designation,nb_enfant_max=nb_enfant_max,niveau=niveau,nb_enfant=0)

    form1=supprimerGroupeForm(request.POST or None)
    if form1.is_valid():
        gr2=Groupe.objects.get(pk=form1['groupe'].value())
        gr2.delete()

    return render(request, "montesory/admin/AjouterGroupe.html", locals())


def ajouterModule(request):
    form=ModuleForm(request.POST or None)
    if form.is_valid():
        form.save()

    form1=SupprimerModuleForm(request.POST or None)
    if form1.is_valid():
        md=Module.objects.get(pk=form1['module'].value())
        md.delete()
    return render(request, "montesory/admin/AjouterModule.html", locals())


def affectation(request):
    aff=Enseignament.objects.all()
    form=AffectationForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, "montesory/admin/Afectation.html", locals(), {'aff':aff, })

def desaffecter(request,id_affectation):
    Enseignament.objects.get(pk=id_affectation).delete()
    return redirect("../affectation")



def ajouterEnfant(request):
    form = EnfantFrom(request.POST or None)

    if form.is_valid():

        gr=Groupe.objects.get(pk=form['groupe'].value())
        nom=form['nom'].value()
        prenom=form['prenom'].value()
        date_N=form['date_N'].value()
        sexe=form['sexe'].value()
        m=Enfant()
        if isinstance(form['parent'],Parent):
          pr=Parent.objects.get(pk=form['parent'].value())
          m=Enfant.objects.create(parent=pr,groupe=gr,nom=nom,prenom=prenom,date_de_naissance=date_N,sexe=sexe)
        else:
           m= Enfant.objects.create( groupe=gr, nom=nom, prenom=prenom, date_de_naissance=date_N, sexe=sexe)
        return redirect("ajouterParent",m.id)

    return render(request, "montesory/admin/AjouterEnfant.html", locals())


def consu_clients(request):
    clients=Enfant.objects.all()
    return render(request, "montesory/admin/Clients.html", {'clients':clients})

def supp_client(request,id_client):
    Enfant.objects.get(pk=id_client).delete()
    return redirect("consu_clients")

def modifierEnfant(request,id_client):
    enfant=Enfant.objects.get(pk=id_client)
    form=ModifierEnfantFrom(request.POST)
    if form.is_valid():
        nom = form['nom'].value()
        prenom = form['prenom'].value()
        date_N = form['date_N'].value()
        sexe = form['sexe'].value()
        if isinstance(form['parent'], Parent):
            pr = Parent.objects.get(pk=form['parent'].value())
            gr = Groupe.objects.get(pk=form['groupe'].value())
            if isinstance(gr,Groupe):
                enfant.parent=pr
                enfant.nom=nom
                enfant.prenom=prenom
                enfant.date_de_naissance=date_N
                enfant.groupe=gr
                enfant.save()
            else:
                enfant.parent = pr
                enfant.nom = nom
                enfant.prenom = prenom
                enfant.date_de_naissance = date_N
                enfant.save()

        else:
            gr = Groupe.objects.get(pk=form['groupe'].value())
            if isinstance(gr, Groupe):
                enfant.nom = nom
                enfant.prenom = prenom
                enfant.date_de_naissance = date_N
                enfant.groupe = gr
                enfant.save()
            else:
                enfant.nom = nom
                enfant.prenom = prenom
                enfant.date_de_naissance = date_N
                enfant.save()
            enfant.nom = nom
            enfant.prenom = prenom
            enfant.date_de_naissance = date_N
            enfant.groupe = gr
            enfant.save()
        return redirect("consu_clients")
    return render(request, "montesory/admin/ModifierEnfant.html", locals(), {'id_client':id_client, })


def client(request,id_client):
    enfant=Enfant.objects.get(pk=id_client)
    return render(request, "montesory/admin/client.html", {'enfant':enfant})

def ajouterParent(request,id_client):
    enfant=Enfant.objects.get(pk=id_client)
    m = Parent()
    form = ParentForm(request.POST or None)
    envoi = False
    if form.is_valid():
        users = User.objects.all()
        first_name = form["first_name"].value()
        last_name = form["last_name"].value()
        email = form["email"].value()
        username = form["username"].value()
        password1 = form['password'].value()
        numero_telephone = form["numero_telephone"].value()
        sexe = form["sexe"].value()
        adr=form['adr'].value()
        adr_tr=form['adr_tr'].value()
        for i in users:
            if username == i.username:
                error = "ce nom d'utlisateur exist deja"
        user, created = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email,
                                                   username=username)
        if created:
            user.set_password(password1)
            for per in Permission.objects.all():
                user.user_permissions.add(per.id)
            user.is_staff = True
            user.save()
            m=Parent.objects.create(user=user, numero_telephone=numero_telephone, sexe=sexe,adr=adr,adr_tr=adr_tr)
        else:
            return HttpResponse("non deja exist")
        envoi = True
        print(m)
        enfant.parent=m
        enfant.save()
        return redirect("client",id_client)

    return render(request, "montesory/admin/AjouterParent.html", locals(), {'enfant':enfant})


def article(request):
    form=ArticleForm(request.POST or None,request.FILES)
    if form.is_valid():
       titre=form['titre'].value()
       discription=form['discription'].value()
       pic=form['pic']
       Article.objects.create(pic=pic,discription=discription,titre=titre)

    return render(request, "montesory/admin/Article.html", locals())

def enseignants(request):
    ens=Enseignant.objects.all()
    return render(request, "montesory/admin/Enseignants.html", {"ens":ens})

def sup_enseignants(request,id_ens):
    Enseignant.objects.get(pk=id_ens).delete()
    return redirect("enseignants")


def enseignant(request,id_ens):
    ens=Enseignant.objects.get(pk=id_ens)
    enseignement=Enseignament.objects.filter(enseignant=ens)
    return render(request, "montesory/admin/Enseignant.html", {'ens':ens, 'enseignement':enseignement, })
def modifier_ens(request,id_ens):
    form3 = ModifierEnseignantForm(request.POST or None)
    en = Enseignant.objects.get(pk=id_ens)
    users=User.objects.all()

    if form3.is_valid():
        first_name1 = form3["first_name"].value()
        last_name1 = form3["last_name"].value()
        email1 = form3["email"].value()
        adr=form3["adr"].value()
        codr_postale=form3["code_postale"].value()
        username=form3["username"].value()
        sexe=form3["sexe"].value()
        for i in users:
            if username == i.username:
                error = "ce nom d'utlisateur exist deja"



        print(codr_postale)
        numero_telephone1 = form3["numero_telephone"].value()
        if first_name1 !="" :
            en.user.first_name = first_name1
        if last_name1 != "":
            en.user.last_name = last_name1
        if email1 !="":
            en.user.email = email1
        if username != "":
            en.user.username = username
        en.user.save()
        if sexe != "":
            en.sexe = sexe
        if numero_telephone1 != "":
            en.numero_telephone = numero_telephone1
        if adr !="":
            en.adr=adr
        if codr_postale != "" :
            en.code_postale=int(codr_postale)
        en.save()
        return redirect("enseignants")
    return render(request, "montesory/admin/ModifierEnseignant.html", locals(), {'en':en})




#-----------------------------------------------------------------------------------------------------------------

def teacher(request,id_user):
    form3 = ModifierEnseignantForm(request.POST or None)
    user=User.objects.get(pk=id_user)
    ens = Enseignant.objects.filter(user=user)
    en =ens[0]
    users = User.objects.all()
    print(en.code_postale)

    form = PasswordChangeCustomForm(request.user,request.POST)

    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request,user)  # Important!
        messages.success(request, 'Your password was successfully updated!')
        return redirect("logout")

    if form3.is_valid():
        first_name1 = form3["first_name"].value()
        last_name1 = form3["last_name"].value()
        email1 = form3["email"].value()
        adr = form3["adr"].value()
        codr_postale = form3["code_postale"].value()
        username = form3["username"].value()
        sexe = form3["sexe"].value()
        for i in users:
            if username == i.username:
                error = "ce nom d'utlisateur exist deja"

        print(codr_postale)
        numero_telephone1 = form3["numero_telephone"].value()
        if first_name1 != "":
            en.user.first_name = first_name1
        if last_name1 != "":
            en.user.last_name = last_name1
        if email1 != "":
            en.user.email = email1
        if username != "":
            en.user.username = username
        en.user.save()
        if sexe != "":
            en.sexe = sexe
        if numero_telephone1 != "":
            en.numero_telephone = numero_telephone1
        if adr != "":
            en.adr = adr
        if codr_postale != "":
            en.code_postale = int(codr_postale)
        en.save()

    return render(request,"montesory/enseignant/Dashboard.html",locals(),{'id_user':id_user,'en':en,})

def consulterEnfant(request,id_user):
    user = User.objects.get(pk=id_user)
    ens = Enseignant.objects.filter(user=user)
    en = ens[0]
    enseignaments=Enseignament.objects.filter(enseignant=en).values_list('groupe', flat=True).distinct()
    groupes=[]
    enfants=[]

    for g in enseignaments:
        groupes.append(Groupe.objects.get(pk=g))
        enfants.append(Enfant.objects.filter(groupe=Groupe.objects.get(pk=g)))




    return render(request,"montesory/enseignant/enfants.html",{'id_user':id_user,'groupes':groupes,'enfants':enfants,})

def statTeacher(request,id_user):
    return render(request,"montesory/enseignant/statistique.html",{'id_user':id_user})



def article(request):
    form = ArticleForm(request.POST,request.FILES)
    sauvegarde = False


    if form.is_valid():

        nom = form.cleaned_data["titre"]

        adresse = form.cleaned_data["discription"]

        photo = form.cleaned_data["pic"]

        Article.objects.create(titre=nom,discription=adresse,pic=photo)
        sauvegarde = True

    return render(request, 'montesory/admin/Article.html', {

        'form': form,

        'sauvegarde': sauvegarde

    })




def voir_contacts(request):
    print(Article.objects.all().__len__())
    articles=Article.objects.all()
    return render(

        request,

        'montesory/article.html',

        {'art': articles,}

    )

def test(request):
    Clients=Enfant.objects.all()
    if request.method == "POST":
        for cl in Clients:
            try:

                print(request.POST["choic "+str(cl.id)])
            except MultiValueDictKeyError :
                print("cccccc",cl.id)

    return render(request,"montesory/test.html",{'clients':Clients})


def test4(request,id_mes):
    mes=MessageA.objects.get(pk=id_mes)
    mes.is_visted=True
    mes.save()
    return redirect("test1")
def test1(request):
    return render(request,"montesory/mes1.html",{'mes':MessageA.objects.all()})

def test2(request):
    return render(request,'montesory/mes2.html',{'mes':MessageB.objects.all()})