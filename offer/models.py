from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class BaseListing(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    make = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    image = models.ImageField(upload_to='listings_images/',blank=True,null=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
class CarListing(BaseListing):
    CATEGORY_CHOICES = [
        ('', 'Избери...'),
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
        ('','Избери...'),
        ('Бензинова','Бензинова'),
        ('Дизелова', 'Дизелова'),
        ('Бензинова/Газ', 'Бензинова/Газ'),
        ('Хибридна','Хибридна'),
        ('Електрическа','Електрическа')
    ]

    transmission_choices = [
        ('', 'Избери...'),
        ('Ръчна','Ръчна'),
        ('Автоматична', 'Автоматична'),
        ('Полуавтоматична', 'Полуавтоматична')
    ]

    model = models.CharField(max_length=100)
    category = models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    kilometers = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=100,choices=fuel_choices)
    transmission = models.CharField(max_length=100,choices=transmission_choices)
    horsepower = models.PositiveIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='car_listings')
class BoatListing(BaseListing):
    BOAT_TYPE_CHOICES = [
        ('', 'Избери...'),
        ('Платноходка', 'Платноходка'),
        ('Моторна лодка', 'Моторна лодка'),
        ('Яхта', 'Яхта'),
        ('Рибарска лодка', 'Рибарска лодка'),
        ('Надуваема лодка', 'Надуваема лодка'),
        ('Скутер', 'Скутер'),
        ('Други', 'Други'),
    ]
    fuel_choices = [
        ('','Избери...'),
        ('Бензинова', 'Бензинова'),
        ('Дизелова', 'Дизелова'),
        ('Бензинова/Газ', 'Бензинова/Газ'),
        ('Хибридна', 'Хибридна'),
        ('Електрическа', 'Електрическа')
    ]
    category = models.CharField(
        max_length=50,
        choices=BOAT_TYPE_CHOICES,
        default='other'
    )
    length = models.DecimalField(max_digits=5, decimal_places=2, help_text="Дължина в метри")
    engine_type = models.CharField(max_length=100, blank=True, null=True,choices=fuel_choices)
    horsepower = models.PositiveIntegerField(help_text="Мощност в к.с.", blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    capacity = models.PositiveIntegerField(help_text="Капацитет на пътници", blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boat_listings')
class MotoListing(BaseListing):
    fuel_choices = [
        ('', 'Избери...'),
        ('Бензинова', 'Бензинова'),
        ('Дизелова', 'Дизелова'),
        ('Бензинова/Газ', 'Бензинова/Газ'),
        ('Хибридна', 'Хибридна'),
        ('Електрическа', 'Електрическа')
    ]
    MOTO_CATEGORIES = [
        ('', 'Избери...'),
        ('Спортен', 'Спортен'),
        ('Нейкед', 'Нейкед'),
        ('Туристически', 'Туристически'),
        ('Круизър', 'Круизър'),
        ('Скутер', 'Скутер'),
        ('Ендуро', 'Ендуро'),
        ('Крос', 'Крос'),
        ('ATV / Бъги', 'ATV / Бъги'),
        ('Други', 'Други'),
    ]

    ENGINE_TYPES = [
        ('', 'Избери...'),
        ('2-stroke', '2 тактов'),
        ('4-stroke', '4 тактов'),
        ('electric', 'Електрически'),
    ]

    TRANSMISSIONS = [
        ('', 'Избери...'),
        ('manual', 'Ръчна'),
        ('automatic', 'Автоматична'),
    ]

    category = models.CharField(max_length=50, choices=MOTO_CATEGORIES)
    engine_size = models.PositiveIntegerField(help_text="в куб. см (cc)")
    engine_type = models.CharField(max_length=20, choices=ENGINE_TYPES)
    fuel_type = models.CharField(max_length=20, choices=fuel_choices)
    transmission = models.CharField(max_length=20, choices=TRANSMISSIONS)
    kilometers = models.PositiveIntegerField(help_text="в километри")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moto_listings')