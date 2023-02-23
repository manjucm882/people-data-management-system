from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class AgeVariant(models.Model):
    age_between = models.IntegerField(
        validators=[
            MinValueValidator(0),  # minimum value allowed
            MaxValueValidator(100),  # maximum value allowed
        ],
        help_text='Enter an age between 0 and 100'
    )

    def __str__(self):
        return str(self.age_between)

    class Meta:
        verbose_name = 'Age Variant'
        verbose_name_plural = 'Age Variants'


class GenderVariant(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.get_gender_display()

    class Meta:
        verbose_name = 'Gender Variant'
        verbose_name_plural = 'Gender Variants'


class Place(models.Model):
    location = models.CharField(max_length=100, help_text='Enter a place name')

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'


class Occupation(models.Model):
    occupation = models.CharField(max_length=100, help_text='Enter an occupation')

    def __str__(self):
        return self.occupation

    class Meta:
        verbose_name = 'Occupation'
        verbose_name_plural = 'Occupations'


class People(models.Model):
    image = models.ImageField(upload_to='statics/people')
    name = models.CharField(max_length=100, help_text='Enter a name')
    age = models.ForeignKey(
        AgeVariant,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='people',
        help_text='Select an age variant'
    )
    gender_type = models.ForeignKey(
        GenderVariant,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='people',
        help_text='Select a gender variant'
    )
    places = models.ForeignKey(
        Place,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='people',
        help_text='Select a place'
    )
    occupation_type = models.ForeignKey(
        Occupation,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='people',
        help_text='Select an occupation'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
