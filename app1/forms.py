
from django import forms
from .models import Employees, Details


class EmployeeForm(forms.ModelForm):

    marital_status = forms.ChoiceField(choices=(('Married', 'Married'), ('Unmarried', 'Unmarried')))
    department = forms.ChoiceField(choices=(('Testing', 'Testing'),('Developer', 'Developer'), ('Ui', 'UI'), ('HR','HR'), ('Marketing', 'Marketing')))
    position = forms.ChoiceField(choices=(('Senior_developer', 'Senior Developer'), ('Junior_developer', 'Junior   Developer'), ( 'Intern','Intern'), ( 'Tester', 'Tester'), ( 'Digital Marketer','Digital marketing')))

    class Meta:
        model = Employees
        fields = ['name', 'email', 'contact', 'address',
                  'skills', 'marital_status', 'department', 'position']
        
    
class DetailsForm(forms.ModelForm):
    
    class Meta:
        model = Details
        fields = [
            'salary', 'feedback',
        ]
        
        
        
