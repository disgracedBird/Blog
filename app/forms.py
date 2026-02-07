from django import forms
from .models import User, Profile, Comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        base_input = (
            "w-min rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-gray-90 placeholder:text-gray-40 shadow-sm transition-all duration-20 focus:border-violet-500 focus:ring-2 focus:ring-violet-500/30 focus:ring-offset-2 focus:shadow-md hover:border-gray-400 outline-none"
        )

        self.fields['username'].widget.attrs.update({'class': base_input})

        self.fields['password'].widget.attrs.update({'class': base_input})

        self.fields['email'].widget.attrs.update({'class': base_input})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        base_input = (
            "w-min rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-gray-90 placeholder:text-gray-40 shadow-sm transition-all duration-20 focus:border-violet-500 focus:ring-2 focus:ring-violet-500/30 focus:ring-offset-2 focus:shadow-md hover:border-gray-400 outline-none"
        )

        self.fields['profile_link'].widget.attrs.update({'class': base_input})

        self.fields['profile_email'].widget.attrs.update({'class': base_input})

        self.fields['profile_number'].widget.attrs.update({'class': base_input})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        base_input = (
            "w-min rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-gray-90 placeholder:text-gray-40 shadow-sm transition-all duration-20 focus:border-violet-500 focus:ring-2 focus:ring-violet-500/30 focus:ring-offset-2 focus:shadow-md hover:border-gray-400 outline-none"
        )

        self.fields['comment'].widget.attrs.update({'class' : base_input})

        self.fields['comment'].required = True
        self.fields['comment'].error_messages = {
            'required': "You can't post an empty comment.",
            'blank': "You can't post an empty comment."
        }

        def clean_text(self):
          comment = self.cleaned_data.get('comment', '').strip()
          if not comment:
            raise forms.ValidationError("You can't post an empty comment.")
          return comment