from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('fullname','email')
    def __init__(self, *args, **kwargs):
       super(RegisterForm, self).__init__(*args, **kwargs)

       del self.fields['password1']
       del self.fields['password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')

class CandidateForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=['address','mobile','profile_pic','pos_applied_for','tenth_percent','graduation','graduation_spcl',  'post_graduation', 'post_graduation_spcl', 'other_qual','currrent_loc','currrent_employer','currrent_ctc','expected_ctc','notice_per','reson_for_leaving','twelfth_percent', 'userform_filled', "intro_vid"]
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':4,
        'cols':50
    }))
    class Meta:
        model = get_user_model()
        fields =['content']