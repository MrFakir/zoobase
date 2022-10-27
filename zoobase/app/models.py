from django.db import models
from django.urls import reverse
from .validators import validate_phone
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True


class Stigmas(models.Model):
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")
    type = models.ForeignKey('TypeStigmas', on_delete=models.PROTECT, verbose_name='Б. клейма',
                             help_text='Выберете тип клейма')
    number = models.IntegerField(verbose_name='Клеймо', help_text='Введите номер клейма')
    tag_number = models.CharField(max_length=20, verbose_name='Бирка',
                                  help_text='Введите номер бирки, при наличии')
    type_animal = models.ForeignKey('TypeAnimals', on_delete=models.PROTECT, verbose_name='Тип животного',
                                    help_text='Выберете тип животного')
    sex = models.ForeignKey('SexTable', on_delete=models.PROTECT, verbose_name='Пол', help_text='Выберете пол')
    the_pet = models.BooleanField(default=False, verbose_name='Домашний', help_text='Домашний/бездомный')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', help_text='Введите номер телефона', )
    master = models.CharField(max_length=255, verbose_name='Хозяин или Куратор',
                              help_text='Введите хозяина (при наличии) или куратора')
    description = models.TextField(verbose_name='Дополнительная информация',
                                   help_text='Введите дополнительную информации при наличии')
    date_created = models.DateField(auto_now_add=True, verbose_name="Дата внесения")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    author = models.CharField(max_length=10, verbose_name='Автор')

    # is_published = models.BooleanField(default=True, verbose_name="Публикация")
    # cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")

    def __str__(self):
        return str(self.type) + str(self.number)

    def get_absolute_url(self):
        return reverse('stigmas', kwargs={'stigmas_slug': self.slug})

    def clean(self):
        self.phone_number = validate_phone(self.phone_number)

    class Meta:
        verbose_name = 'Клейма'
        verbose_name_plural = 'Клейма'
        ordering = ['id']


class TypeStigmas(models.Model):
    title = models.CharField(max_length=5, db_index=True, verbose_name="Название", help_text='Первые буквы клейма')
    slug = models.SlugField(max_length=5, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('type_stigmas', kwargs={'type_stigmas_slug': self.slug})

    class Meta:
        verbose_name = 'Буквы клейма'
        verbose_name_plural = 'Буквы клейм'
        ordering = ['title']


class SexTable(models.Model):
    sex = models.CharField(max_length=5, db_index=True, verbose_name="Пол", help_text='Пол животного')
    slug = models.SlugField(max_length=5, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.sex

    def get_absolute_url(self):
        return reverse('sex', kwargs={'sex_slug': self.slug})

    class Meta:
        verbose_name = 'Пол животного'
        verbose_name_plural = 'Пол животного'
        ordering = ['sex']


class TypeAnimals(models.Model):
    type = models.CharField(max_length=10, db_index=True, verbose_name="Вид", help_text='Вид животного')
    slug = models.SlugField(max_length=5, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('type', kwargs={'type_slug': self.slug})

    class Meta:
        verbose_name = 'Вид животного'
        verbose_name_plural = 'Вид животного'
        ordering = ['id']

# class MainMenu(models.Model):
#     name = models.CharField(max_length=25, db_index=True, verbose_name="Пункт меню")
#     slug = models.SlugField(max_length=25, unique=True, db_index=True, verbose_name="URL", help_text='Имя класса')
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('name', kwargs={'name_slug': self.slug})
#
#     class Meta:
#         verbose_name = 'Меню'
#         verbose_name_plural = 'Меню'
#         ordering = ['name']
