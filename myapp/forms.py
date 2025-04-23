from django import forms
from .models import reg
from .models import course
from .models import subject
from .models import paper
from .models import resultmodel
class regfrom(forms.ModelForm):
    class Meta:
        model = reg
        fields = '__all__'
class coursefrom(forms.ModelForm):
    class Meta:
        model=course
        fields='__all__'
class subjectfrom(forms.ModelForm):
    class Meta:
        model=subject
        fields='__all__'   
class paperfrom(forms.ModelForm):
    class Meta:
        model=paper
        fields='__all__'
class resultfrom(forms.ModelForm):
    class Meta:
        model=resultmodel
        fields='__all__'
