from random import randint

from .models import *


def test_data(uniq_number, uniq_tag):
    while True:
        uniq_number_now = randint(100, 2500)
        if uniq_number_now in uniq_number:
            continue
        else:
            uniq_number.append(uniq_number_now)
            break

    while True:
        uniq_tag_now = randint(100, 2541)
        if uniq_tag_now in uniq_tag:
            continue
        else:
            uniq_tag.append(uniq_number_now)
            break
    data = Stigmas(
        type_id=[1, 2][randint(0, 1)],
        slug='',
        number=uniq_number_now,
        tag_number=str(uniq_tag_now),
        type_animal_id=[1, 2, 3][randint(0, 2)],
        sex_id=[1, 2][randint(0, 1)],
        the_pet=[True, False][randint(0, 1)],
        phone_number='+79' + str(randint(111111111, 999999999)),
        master=['Стеша', 'Гера', 'Оля', 'Какие-то волонтеры'][randint(0, 3)],
        description=['Подробное описание', 'Не подробное описание'][randint(0, 1)],
        author='testData',
    )

    return {'data': data, 'uniq_number': uniq_number, 'uniq_tag': uniq_tag}


def start_test_data():
    uniq_number = []
    uniq_tag = []
    for i in range(0, 2000):
        data = test_data(uniq_number=uniq_number, uniq_tag=uniq_tag)
        uniq_number = data['uniq_number']
        uniq_tag = data['uniq_tag']
        db_date = data['data']
        db_date.clean()
        db_date.save()
