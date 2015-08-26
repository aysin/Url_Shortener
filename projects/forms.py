# Aysin Oruz 

from django import forms

class UrlForm(forms.Form):

	url = forms.URLField(label='Url', max_length=500)

	def __init__(self, *args, **kwargs):
		super(UrlForm, self).__init__(*args, **kwargs)

		for field in self.base_fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

		self.fields['url'].widget.attrs['placeholder'] = 'http://aysinoruz.com'
		self.fields['url'].widget.attrs['value'] = 'http://aysinoruz.com'
