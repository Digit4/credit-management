from django import forms
from django.core import validators
from basicfunc.views import Participant


CHOICES = [Participant.objects.all()[0].email]


class TransferCredits(forms.Form):
	amount = forms.IntegerField(max_value=1000, label="Enter amount to transfer")
	sender = forms.EmailField(widget=forms.HiddenInput(), label="")
	creditor_email = forms.EmailField(widget=forms.HiddenInput(), label="")

	def clean_sender(self):
		cleaned_data = super(TransferCredits, self).clean()
		s_email = cleaned_data['sender']
		s_obj = Participant.objects.filter(email=s_email)[0]
		if s_obj.credit_points < cleaned_data['amount']:
			print('Should not print')
			raise forms.ValidationError("This user does not have enough credits")
		return cleaned_data['sender']

	def clean_creditor_email(self):
		cleaned_data = super(TransferCredits, self).clean()
		amt = cleaned_data['amount']
		em = cleaned_data['creditor_email']
		se = cleaned_data['sender']
		# Find the user's credit points for validation with amount
		usr = Participant.objects.filter(email=se)
		if not usr:
			print("no user is selected.")
			raise forms.ValidationError("Please select a user")
		
		print(cleaned_data)
		return (cleaned_data['creditor_email'])
