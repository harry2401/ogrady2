from django                                 import forms
from .models                                import Site, Photo,  EnquiryB
#from .models                                import Site, Photo
#from .models                                import PhotoB

class advertUpdateForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ( 'notice' ,)
        #fields = ( 'notice' ,'contact_info' )

class noteUpdateForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ('note',)

class PhotoInsertForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'cover')

class PhotopriorityUpdateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('priority',)

class PhototitleUpdateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title',)

class EnquiryInsertForm(forms.ModelForm):
    class Meta:
        model = EnquiryB
        fields = ('content',)

class EnquirypriorityUpdateForm(forms.ModelForm):
    class Meta:
        model = EnquiryB
        fields = ('priority',)

"""
class PhotoauthorUpdateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('author',)
"""
