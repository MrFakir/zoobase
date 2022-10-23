# Generated by Django 4.1.2 on 2022-10-20 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SexTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(db_index=True, help_text='Пол животного', max_length=5, verbose_name='Пол')),
                ('slug', models.SlugField(max_length=5, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Пол животного',
                'verbose_name_plural': 'Пол животного',
                'ordering': ['sex'],
            },
        ),
        migrations.CreateModel(
            name='TypeAnimals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(db_index=True, help_text='Вид животного', max_length=10, verbose_name='Вид')),
                ('slug', models.SlugField(max_length=5, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Вид животного',
                'verbose_name_plural': 'Вид животного',
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='TypeStigmas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, help_text='Первые буквы клейма', max_length=5, verbose_name='Название')),
                ('slug', models.SlugField(max_length=5, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Буквы клейма',
                'verbose_name_plural': 'Буквы клейм',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Stigmas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, verbose_name='URL')),
                ('number', models.IntegerField(help_text='Введите номер клейма', verbose_name='Номер клейма')),
                ('tag_number', models.CharField(help_text='Введите номер бирки, при наличии', max_length=20, verbose_name='Номер бирки')),
                ('the_pet', models.BooleanField(default=False, help_text='Домашний/бездомный', verbose_name='Домашний')),
                ('phone_number', models.CharField(help_text='Введите номер телефона', max_length=20, verbose_name='Номер телефона')),
                ('master', models.CharField(help_text='Введите хозяина (при наличии) или куратора', max_length=255, verbose_name='Хозяин или Куратор')),
                ('description', models.TextField(help_text='Введите дополнительную информации при наличии', verbose_name='Дополнительная информация')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('author', models.CharField(max_length=10, verbose_name='Автор')),
                ('sex', models.ForeignKey(help_text='Выберете пол', on_delete=django.db.models.deletion.PROTECT, to='app.sextable', verbose_name='Пол')),
                ('type', models.ForeignKey(help_text='Выберете тип клейма', on_delete=django.db.models.deletion.PROTECT, to='app.typestigmas', verbose_name='Тип клейма')),
                ('type_animal', models.ForeignKey(help_text='Выберете тип животного', on_delete=django.db.models.deletion.PROTECT, to='app.typeanimals', verbose_name='Тип животного')),
            ],
            options={
                'verbose_name': 'Клейма',
                'verbose_name_plural': 'Клейма',
                'ordering': ['number'],
            },
        ),
    ]