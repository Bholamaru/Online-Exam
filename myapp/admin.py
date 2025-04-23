from django.contrib import admin
from .models import reg
from.models import course
from .models import subject
from .models import paper
from .models import resultmodel
# Register your models here.
admin.site.register(reg)
admin.site.register(course)
admin.site.register(subject)
admin.site.register(paper)
admin.site.register(resultmodel)