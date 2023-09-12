from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'price', 'image', 'category',)
        # exclude = ('date_start',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if 'казино' or 'криптовалюта' or 'крипта' or 'биржа' or 'дешево' or 'бесплатно' or 'обман' or 'полиция' or 'радар' in cleaned_data:
            raise forms.ValidationError('Такое название нельзя использовать!')

        return cleaned_data


