from django import forms    
    
class Student(forms.Form):  
        firstname = forms.CharField(label="Enter first name",max_length=50)  
        lastname  = forms.CharField(label="Enter last name", max_length = 10)  
        email     = forms.EmailField(label="Enter Email")  
        file      = forms.FileField() # for creating file input    

from myapp.models import Employee  
  
class Employee(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__" 
