from django import forms
from .models import *

#form to update new expenditures mapped to each models
class Expense_form1(forms.ModelForm):
	activity = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the expense activity'}),required=True,max_length=50)
	personal_exp = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the personal expense amount'}),required=False)
	sharing_exp= forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the shared expense amount'}),required=False)
	
	class Meta():
		model = Ram;
		fields = ['activity','personal_exp','sharing_exp']


class Expense_form2(forms.ModelForm):
	activity = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the expense activity'}),required=True,max_length=50)
	personal_exp = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the personal expense amount'}),required=False)
	sharing_exp= forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the shared expense amount'}),required=False)
	
	class Meta():
		model = Shyam;
		fields = ['activity','personal_exp','sharing_exp']