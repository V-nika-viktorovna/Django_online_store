from django.core.validators import ValidationError
from django.forms import ModelForm

from catalog.models import Product

unacceptables = [
    'казино', 'криптовалюта', 'крипта',
    'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]


class ProductStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })

            if name == 'name':
                field.widget.attrs.update({
                    'placeholder': 'Введите название'
                })

            if name == 'description':
                field.widget.attrs.update({
                    'placeholder': 'Введите описание'
                })


class ProductCreateForms(ProductStyleMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'purchase_price')

    def clean_purchase_price(self):
        purchase_price = self.cleaned_data.get('purchase_price')
        if purchase_price <= 0:
            raise ValidationError('Цена не может быть нулувой или отрицательной')
        return purchase_price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for unacceptable in unacceptables:
            if unacceptable in name or unacceptable in description:
                raise ValidationError(f'Название или описание продукта не может содержать "{unacceptable}"')


class ProductModeratorForms(ProductStyleMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'publication_status',)
