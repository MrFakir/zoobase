# Generated by Django 4.1.2 on 2022-10-23 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_stigmas_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stigmas',
            name='number',
            field=models.IntegerField(help_text='Введите номер клейма', verbose_name='Клеймо'),
        ),
        migrations.AlterField(
            model_name='stigmas',
            name='tag_number',
            field=models.CharField(help_text='Введите номер бирки, при наличии', max_length=20, verbose_name='Бирка'),
        ),
        migrations.AlterField(
            model_name='stigmas',
            name='type',
            field=models.ForeignKey(help_text='Выберете тип клейма', on_delete=django.db.models.deletion.PROTECT, to='app.typestigmas', verbose_name='Б. клейма'),
        ),
    ]
