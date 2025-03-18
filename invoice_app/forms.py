from django import forms


class addressform(forms.Form):
    org_name = forms.CharField(max_length=255, label="Organization name")
    line1 = forms.CharField(max_length=255, label="Address Line 01")
    line2 = forms.CharField(max_length=255, label="Address Line 02")
    line3 = forms.CharField(max_length=255, label="Address Line 03")


class InvoiceForm(forms.Form):
    customer_number = forms.CharField(max_length=15, label="Customer Details")


class ItemForm(forms.Form):
    name = forms.CharField(max_length=255, label="Item Name")
    description = forms.CharField(max_length=255, label="Description")
    qty = forms.IntegerField(label="Quantity")
    price = forms.FloatField(label="Price")
