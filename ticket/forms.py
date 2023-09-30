from django import forms

from .models import Ticket

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=['title','description']
        widgets={
            'title':forms.TextInput(attrs={
                'placeholder':'Enter a title',
                'class':'px-6 py-4 rounded-lg border border-solid border-gray-600 w-full'
            }),
            'description':forms.Textarea(attrs={
                'placeholder':'Enter a description for the issue you are facing',
                'class':'h-48 w-full px-6 py-6 rounded-lg border border-solid border-gray-600'
            })

        }


class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=['title','description']
        widgets={
            'title':forms.TextInput(attrs={
                # 'placeholder':'Enter a title',
                'class':'px-6 py-4 rounded-lg border border-solid border-gray-600 w-full'
            }),
            'description':forms.Textarea(attrs={
                # 'placeholder':'Enter a description for the issue you are facing',
                'class':'h-48 w-full px-6 py-6 rounded-lg border border-solid border-gray-600'
            })

        }
        