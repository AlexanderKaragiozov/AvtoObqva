from django import forms

import offer.models
from offer.models import *


class CarSearchForm(forms.Form):
    CATEGORY_CHOICES = [
        ('Седан', 'Седан'),
        ('Хечбек', 'Хечбек'),
        ('SUV', 'SUV'),
        ('Купе', 'Купе'),
        ('Кабриолет', 'Кабриолет'),
        ('Комби', 'Комби'),
        ('Ван', 'Ван'),
        ('Пикап', 'Пикап'),
        ('Други', 'Други'),
    ]

    fuel_choices = [
        ('Бензинова', 'Бензинова'),
        ('Дизелова', 'Дизелова'),
        ('Бензинова/Газ', 'Бензинова/Газ'),
        ('Хибридна', 'Хибридна'),
        ('Електрическа', 'Електрическа')
    ]

    transmission_choices = [
        ('Ръчна', 'Ръчна'),
        ('Автоматична', 'Автоматична'),
        ('Полуавтоматична', 'Полуавтоматична')
    ]
    title = forms.CharField(
        required=False,
        label='Заглавие на обява',
        widget=forms.TextInput(attrs={'placeholder': 'Пример: Голф 5 1.9 TDI'})
    )
    category = forms.ChoiceField(
        required=False,
        choices=[('', 'Всички')] + CATEGORY_CHOICES,
        label='Категория',
        widget=forms.Select(attrs={'placeholder': 'Изберете категория'})
    )
    make = forms.CharField(
        required=False,
        label='Марка',
        widget=forms.TextInput(attrs={'placeholder': 'Пример: Volkswagen'})
    )
    model = forms.CharField(
        required=False,
        label='Модел',
        widget=forms.TextInput(attrs={'placeholder': 'Пример: Golf'})
    )
    year = forms.IntegerField(
        required=False,
        label='Година',
        widget=forms.NumberInput(attrs={'placeholder': 'Пример: 2010'})
    )
    kilometers = forms.IntegerField(
        required=False,
        label='Километри',
        widget=forms.NumberInput(attrs={'placeholder': 'Пример: 200000'})
    )
    fuel_type = forms.ChoiceField(
        required=False,
        choices=[('', 'Всички')] + fuel_choices,
        label='Горивна система',
        widget=forms.Select(attrs={'placeholder': 'Изберете гориво'})
    )
    transmission = forms.ChoiceField(
        required=False,
        choices=[('', 'Всички')] + transmission_choices,
        label='Скоростна кутия',
        widget=forms.Select(attrs={'placeholder': 'Пример: Ръчна'})
    )
    horsepower = forms.CharField(
        required=False,
        label='Конски сили',
        widget=forms.TextInput(attrs={'placeholder': 'Пример: 105'})
    )
    min_price = forms.DecimalField(
        required=False,
        label='Минимална цена',
        widget=forms.NumberInput(attrs={'placeholder': 'Пример: 2000'})
    )
    max_price = forms.DecimalField(
        required=False,
        label='Максимална цена',
        widget=forms.NumberInput(attrs={'placeholder': 'Пример: 10000'})
    )
    location = forms.CharField(
        required=False,
        label='Локация',
        widget=forms.TextInput(attrs={'placeholder': 'Пример: София'})
    )

class BoatSearchForm(forms.Form):
    BOAT_TYPE_CHOICES = [
        ('', 'Избери тип'),
        ('Платноходка', 'Платноходка'),
        ('Моторна лодка', 'Моторна лодка'),
        ('Яхта', 'Яхта'),
        ('Рибарска лодка', 'Рибарска лодка'),
        ('Надуваема лодка', 'Надуваема лодка'),
        ('Скутер', 'Скутер'),
        ('Други', 'Други'),
    ]
    fuel_choices = [
        ('Бензинова', 'Бензинова'),
        ('Дизелова', 'Дизелова'),
        ('Бензинова/Газ', 'Бензинова/Газ'),
        ('Хибридна', 'Хибридна'),
        ('Електрическа', 'Електрическа')
    ]
    keyword = forms.CharField(
        required=False,
        label='Заглавие на обява',
        widget=forms.TextInput(attrs={'placeholder': 'Заглавие или ключова дума'})
    )
    make = forms.CharField(
        required=False,
        label='Марка',
        widget=forms.TextInput(attrs={'placeholder': 'Пример: Yamaha'})
    )
    boat_type = forms.ChoiceField(
        required=False,
        choices=BOAT_TYPE_CHOICES,
        label='Тип лодка'
    )
    length = forms.DecimalField(
        required=False,
        label='Дължина (м)',
        widget=forms.NumberInput(attrs={'placeholder': 'Пример: 8.5', 'step': '0.1'})
    )
    engine_type = forms.ChoiceField(
        required=False,
        label='Горивна система',
        choices=[('', 'Всички')] + fuel_choices,
        widget=forms.Select(attrs={'placeholder': 'Пример: Вътрешен'})
    )
    engine_power = forms.IntegerField(
        required=False,
        label='Мощност (к.с.)',
        widget=forms.NumberInput(attrs={'placeholder': 'Пример: 200'})
    )
    material = forms.CharField(
        required=False,
        label='Материал',
        widget=forms.TextInput(attrs={'placeholder': 'Пример: Фибростъкло'})
    )
    capacity = forms.IntegerField(
        required=False,
        label='Капацитет',
        widget=forms.NumberInput(attrs={'placeholder': 'Пример: 6'})
    )
    year = forms.IntegerField(
        required=False,
        label='Година',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Пример: 2015',
            'min': 1900,
            'max': 2025
        })
    )
    min_price = forms.DecimalField(
        required=False,
        label='Минимална цена (€)',
        widget=forms.NumberInput(attrs={'placeholder': 'Пример: 10000'})
    )
    max_price = forms.DecimalField(
        required=False,
        label='Максимална цена (€)',
        widget=forms.NumberInput(attrs={'placeholder': 'Пример: 50000'})
    )
    location = forms.CharField(
        required=False,
        label='Местоположение',
        widget=forms.TextInput(attrs={'placeholder': 'Пример: Варна'})
    )


ENGINE_TYPES = [
    ('', 'Избери тип двигател'),
    ('2-stroke', '2 тактов'),
    ('4-stroke', '4 тактов'),
    ('electric', 'Електрически'),
]

TRANSMISSIONS = [
    ('', 'Избери'),
    ('manual', 'Ръчна'),
    ('automatic', 'Автоматична'),
]

class MotoSearchForm(forms.Form):
    CATEGORY_CHOICES = [
        ('', 'Избери категория'),
        ('sport', 'Спортен'),
        ('naked', 'Нейкед'),
        ('touring', 'Туристически'),
        ('cruiser', 'Круизър'),
        ('scooter', 'Скутер'),
        ('enduro', 'Ендуро'),
        ('cross', 'Крос'),
        ('atv', 'ATV / Бъги'),
        ('other', 'Други'),
    ]
    fuel_choices = [
        ('', 'Избери гориво'),
        ('Бензинова', 'Бензинова'),
        ('Дизелова', 'Дизелова'),
        ('Бензинова/Газ', 'Бензинова/Газ'),
        ('Хибридна', 'Хибридна'),
        ('Електрическа', 'Електрическа')
    ]
    title = forms.CharField(
        required=False,
        label='Заглавие',
        widget=forms.TextInput(attrs={'placeholder': 'Yamaha'})
    )
    category = forms.ChoiceField(
        required=False,
        choices=CATEGORY_CHOICES,
        label='Категория'
    )
    make = forms.CharField(
        required=False,
        label='Марка',
        widget=forms.TextInput(attrs={'placeholder': 'Пример: Honda'})
    )
    engine = forms.IntegerField(
        required=False,
        label='Обем на двигателя (cc)',
        min_value=50,
        widget=forms.NumberInput(attrs={'placeholder': 'Пример: 600', 'step': 1})
    )
    engine_type = forms.ChoiceField(
        required=False,
        choices=ENGINE_TYPES,
        label='Тип двигател'
    )
    fuel_type = forms.ChoiceField(
        required=False,
        label='Горивна система',
        choices=fuel_choices,
        widget=forms.Select(attrs={'placeholder':'Избери гориво'})
    )
    kilometers = forms.IntegerField(
        required=False,
        label='Километри',
        widget=forms.NumberInput(attrs={'placeholder': 'Пример: 15000'})
    )
    year = forms.IntegerField(
        required=False,
        label='Година',
        min_value=1900,
        max_value=2025,
        widget=forms.NumberInput(attrs={'placeholder': 'Пример: 2020'})
    )
    transmission = forms.ChoiceField(
        required=False,
        choices=TRANSMISSIONS,
        label='Скоростна кутия'
    )
    min_price = forms.DecimalField(
        required=False,
        label='Минимална цена (€)',
        min_value=0,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Пример: 2000', 'step': '0.01'})
    )
    max_price = forms.DecimalField(
        required=False,
        label='Максимална цена (€)',
        min_value=0,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Пример: 10000', 'step': '0.01'})
    )
    location = forms.CharField(
        required=False,
        label='Местоположение',
        widget=forms.TextInput(attrs={'placeholder': 'Пример: Пловдив'})
    )


class CarListingCreationForm(forms.ModelForm):
    class Meta:
        labels = {
            'title': 'Име на обява',
            'category': 'Категория',
            'make': 'Марка',
            'model': 'Модел',
            'year': 'Година',
            'fuel_type': 'Горивна система',
            'price': 'Цена (€)',
            'spec': 'Пробег (км)',
            'fuel': 'Гориво',
            'transmission': 'Скорости',
            'location': 'Местоположение',
            'description': 'Описание',
            'image': 'Качете снимки',
            'kilometers': 'Километри'
        }
        model = offer.models.CarListing
        exclude = ('owner', 'views')
        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'title',
                'class': 'form-control',
                'placeholder': 'Пример: Хонда 2012 СПЕШНО!',
                'required': 'required'
            }),
            'category': forms.Select(attrs={
                'id': 'category',
                'class': 'form-control',
                'placeholder': 'Избери',
                'required': 'required'
            }),

            'make': forms.TextInput(attrs={
                'id': 'make',
                'class': 'form-control',
                'placeholder': 'Пример: BMW',
                'required': 'required'
            }),
            'model': forms.TextInput(attrs={
                'id': 'model',
                'class': 'form-control',
                'placeholder': 'Пример: 320i',
                'required': 'required'
            }),
            'year': forms.NumberInput(attrs={
                'id': 'year',
                'class': 'form-control',
                'placeholder': 'Пример: 2018',
                'min': 1900,
                'max': 2025,
                'required': 'required'
            }),
            'fuel_type': forms.Select(attrs={
                'id': 'fuel_type',
                'class': 'form-control',
                'placeholder': 'Избери'
            }),
            'price': forms.NumberInput(attrs={
                'id': 'price',
                'class': 'form-control',
                'placeholder': 'Пример: 15000',
                'min': 0,
                'step': 0.01,
                'required': 'required'
            }),
            'fuel': forms.Select(attrs={
                'id': 'fuel',
                'class': 'form-select'
            }),
            'transmission': forms.Select(attrs={
                'id': 'transmission',
                'class': 'form-select'
            }),
            'location': forms.TextInput(attrs={
                'id': 'location',
                'class': 'form-control',
                'placeholder': 'Пример: София'
            }),
            'description': forms.Textarea(attrs={
                'id': 'description',
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Опишете състояние, обслужване…'
            }),
            'image': forms.ClearableFileInput(attrs={
                'id': 'image',
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'kilometers': forms.NumberInput(attrs={
                'id': 'kilometers',
                'class': 'form-control',
                'placeholder': "Пример: 100000"
            }),
            'horsepower': forms.NumberInput(attrs={
                'id': 'horsepower',
                'class': 'form-control',
                'placeholder': "Пример: 171"
            })
        }
class BoatListingCreationForm(forms.ModelForm):
    class Meta:
        model = BoatListing
        exclude = ('owner', 'views', 'created_at')  # тези се попълват автоматично

        labels = {
            'title': 'Име на обява',
            'category': 'Тип лодка',
            'make': 'Марка',
            'year': 'Година',
            'price': 'Цена (€)',
            'location': 'Местоположение',
            'description': 'Описание',
            'image': 'Качете снимки',
            'length': 'Дължина (м)',
            'engine_type': 'Горивна система',
            'horsepower': 'Мощност (к.с.)',
            'material': 'Материал',
            'capacity': 'Капацитет (пътници)',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пример: Моторна яхта Bavaria 36'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'make': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пример: Bavaria'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1900,
                'max': 2025,
                'placeholder': 'Пример: 2015'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'step': 0.01,
                'placeholder': 'Пример: 35000'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пример: Бургас'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Опишете състоянието, оборудването и т.н.'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'length': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 0.01,
                'placeholder': 'Пример: 10.50'
            }),
            'engine_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'horsepower': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пример: 200'
            }),
            'material': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пример: Фибростъкло'
            }),
            'capacity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пример: 8'
            }),
        }

class MotoListingCreationForm(forms.ModelForm):
    class Meta:
        model = MotoListing
        exclude = ('owner', 'views')
        labels = {
            'title': 'Име на обява',
            'category': 'Категория',
            'make': 'Марка',
            'year': 'Година',
            'engine_size': 'Обем на двигателя (cc)',
            'engine_type': 'Тип двигател',
            'fuel_type': 'Горивна система',
            'transmission': 'Скоростна кутия',
            'kilometers': 'Километри',
            'price': 'Цена (€)',
            'location': 'Местоположение',
            'description': 'Описание',
            'image': 'Качете снимка',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'title',
                'class': 'form-control',
                'placeholder': 'Пример: Yamaha R6 2015',
                'required': 'required'
            }),
            'category': forms.Select(attrs={
                'id': 'category',
                'class': 'form-select',
                'required': 'required'
            }),
            'make': forms.TextInput(attrs={
                'id': 'make',
                'class': 'form-control',
                'placeholder': 'Пример: Honda',
                'required': 'required'
            }),
            'year': forms.NumberInput(attrs={
                'id': 'year',
                'class': 'form-control',
                'placeholder': 'Пример: 2020',
                'min': 1900,
                'max': 2025,
                'required': 'required'
            }),
            'engine_size': forms.NumberInput(attrs={
                'id': 'engine_size',
                'class': 'form-control',
                'placeholder': 'Пример: 600',
                'required': 'required'
            }),
            'engine_type': forms.Select(attrs={
                'id': 'engine_type',
                'class': 'form-select',
                'required': 'required'
            }),
            'fuel_type': forms.Select(attrs={
                'id': 'fuel_type',
                'class': 'form-select',
                'required': 'required'
            }),
            'transmission': forms.Select(attrs={
                'id': 'transmission',
                'class': 'form-select',
                'required': 'required'
            }),
            'kilometers': forms.NumberInput(attrs={
                'id': 'kilometers',
                'class': 'form-control',
                'placeholder': 'Пример: 25000'
            }),
            'price': forms.NumberInput(attrs={
                'id': 'price',
                'class': 'form-control',
                'placeholder': 'Пример: 4500',
                'min': 0,
                'step': 0.01,
                'required': 'required'
            }),
            'location': forms.TextInput(attrs={
                'id': 'location',
                'class': 'form-control',
                'placeholder': 'Пример: Варна'
            }),
            'description': forms.Textarea(attrs={
                'id': 'description',
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Опишете мотоциклета, поддръжка, състояние…'
            }),
            'image': forms.FileInput(attrs={
                'id': 'image',
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }