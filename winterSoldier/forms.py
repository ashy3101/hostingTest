from django import forms

class myform1(forms.Form):
    name=forms.CharField(label="Name", max_length=50)
    mobile=forms.IntegerField(label="Mobile")