from django import forms 

class PostForm(forms.Form):

	title       = forms.CharField(
									label="Post Title",
									max_length=100,
									widget=forms.TextInput(attrs={'placeholder':'Enter Post Title','class':'form-control'})
								 )
	description = forms.CharField(
									label="Post Description",
									widget=forms.Textarea(attrs={'placeholder':'Enter Post Description','class':'form-control','rows':5})
								 )