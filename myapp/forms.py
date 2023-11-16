from django import forms

class CartForm(forms.Form):
    quantity = forms.IntegerField(initial='1')
    product_id = forms.IntegerField(widget=forms.HiddenInput)

    def _init_(self,request,args,*kwargs):
        self.request=request
        super(CartForm,self)._init_(args,*kwargs)