from django import forms
from .models import Product, Level, Angle, Material


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        materials = Material.objects.all()
        angles = Angle.objects.all()
        levels = Level.objects.all()

        friendly_names_materials = [(m.id, m.get_friendly_name()) for m in materials]
        friendly_names_angles = [(a.id, a.get_friendly_name()) for a in angles]
        friendly_names_levels = [(l.id, l.get_friendly_name()) for l in levels]

        self.fields['material'].choices = friendly_names_materials
        self.fields['angle'].choices = friendly_names_angles
        self.fields['level'].choices = friendly_names_levels
