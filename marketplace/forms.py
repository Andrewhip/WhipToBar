from django import forms
from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    # Добавляем поле images вручную, чтобы оно было доступно в форме
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'allow_multiple_selected': True}),
        required=False,
        label='Добавить изображения'
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'images']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем атрибут 'multiple' к полю изображений
        self.fields['images'].widget.attrs.update({'multiple': 'true'})

    def clean_images(self):
        images = self.files.getlist('images')
        if len(images) > 5:
            raise forms.ValidationError("Можно загрузить не более 5 изображений.")
        return images

