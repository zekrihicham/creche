from django.contrib import admin

# Register your models here.
from montesory.models import *


admin.site.register(Enseignant)
admin.site.register(Parent)
admin.site.register(Enfant)
admin.site.register(Groupe)


admin.site.register(MessageA)
admin.site.register(MessageB)

admin.site.register(Module)
admin.site.register(Enseignament)
admin.site.register(RemarqueEnseignant)
admin.site.register(RemarqueParent)
admin.site.register(Article)






