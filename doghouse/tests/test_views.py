import json

import pytest

from doghouse.models import Animal


class TestViewDoghouse:

    @pytest.fixture
    def animal(self):
        return {
            'name': 'Ada',
            'specie': 'cat',
            'gender': 'female',
            'age': 'kitten',
            'size': 'small',
            'hair': 'short',
            'color': 'preto',
            'description': 'new baby',
            'address': 'SP',
            'adopted': False
        }

    @pytest.fixture
    def animal_saved(self):
        animal = Animal.objects.create(
            name='Ada',
            specie='cat',
            gender='female',
            age='kitten',
            size='small',
            hair='short',
            color='preto',
            description='new baby',
            address='SP',
            adopted=False
        )

    @pytest.mark.django_db
    def test_post_animal(self, client, animal):
        response = client.post('/animals/', animal)

        assert response.status_code == 201
        assert response.json() == animal

    @pytest.mark.parametrize('field', [
        'name', 'specie', 'gender', 'age', 'size',
        'hair', 'color', 'description', 'address'
    ])
    @pytest.mark.django_db
    def test_post_animal_with_empty_fields(self, client, field, animal):
        del animal[field]
        response = client.post('/animals/', animal)

        assert response.status_code == 400
        assert response.json() == {field: ['Este campo é obrigatório.']}

    @pytest.mark.parametrize('field', [
        'specie', 'gender', 'age', 'size', 'hair'
    ])
    @pytest.mark.django_db
    def test_post_animal_with_invalid_fields_choices(
        self, client, field, animal
    ):
        animal[field] = 'invalid input'
        response = client.post('/animals/', animal)

        assert response.status_code == 400
        assert response.json() == {
            field: ['"invalid input" não é um escolha válido.']
        }

    @pytest.mark.django_db
    def test_get_list_animals(self, client, animal_saved):
        response = client.get('/animals/')
        assert response.status_code == 200
        assert response.json() == [{
            'name': 'Ada',
            'specie': 'cat',
            'gender': 'female',
            'age': 'kitten',
            'size': 'small',
            'hair': 'short',
            'color': 'preto',
            'description': 'new baby',
            'address': 'SP',
            'adopted': False
        }]

    @pytest.mark.django_db
    def test_get_one_animal(self, client, animal_saved):
        response = client.get('/animals/1/')

        assert response.status_code == 200
        assert response.json() == {
            'name': 'Ada',
            'specie': 'cat',
            'gender': 'female',
            'age': 'kitten',
            'size': 'small',
            'hair': 'short',
            'color': 'preto',
            'description': 'new baby',
            'address': 'SP',
            'adopted': False
        }

    @pytest.mark.django_db
    def test_get_one_animal_not_found(self, client, animal_saved):
        response = client.get('/animals/20/')

        assert response.status_code == 404
        assert response.json() == {'detail': 'Não encontrado.'}

    @pytest.mark.django_db
    def test_put_one_animal(self, client,  animal, animal_saved):
        animal['name'] = 'Ada Lovelace'
        animal['description'] = 'adopted'
        animal['adopted'] = True

        response = client.put(
            '/animals/1/', data=json.dumps(animal),
            content_type='application/json'
        )

        assert response.status_code == 200
        assert response.json() == {
            'name': 'Ada Lovelace',
            'specie': 'cat',
            'gender': 'female',
            'age': 'kitten',
            'size': 'small',
            'hair': 'short',
            'color': 'preto',
            'description': 'adopted',
            'address': 'SP',
            'adopted': True
        }

    @pytest.mark.django_db
    def test_put_one_animal_not_found(self, client, animal_saved):
        response = client.put('/animals/20/')

        assert response.status_code == 404
        assert response.json() == {'detail': 'Não encontrado.'}

    @pytest.mark.parametrize('field', [
        'name', 'specie', 'gender', 'age', 'size',
        'hair', 'color', 'description', 'address'
    ])
    @pytest.mark.django_db
    def test_put_one_animal_with_empty_fields(
        self, client, field, animal, animal_saved
    ):
        del animal[field]

        response = client.put(
            '/animals/1/',
            data=json.dumps(animal),
            content_type='application/json'
        )

        assert response.status_code == 400
        assert response.json() == {
            field: ['Este campo é obrigatório.']
        }

    @pytest.mark.parametrize('field', [
        'specie', 'gender', 'age', 'size', 'hair'
    ])
    @pytest.mark.django_db
    def test_put_one_animal_with_invalid_fields(
        self, client, field, animal, animal_saved
    ):
        animal[field] = 'invalid input'

        response = client.put(
            '/animals/1/',
            data=json.dumps(animal),
            content_type='application/json')

        assert response.status_code == 400
        assert response.json() == {
            field: ['"invalid input" não é um escolha válido.']
        }

    @pytest.mark.django_db
    def test_delete_one_animal(self, client, animal_saved):
        response = client.delete('/animals/1/')

        assert response.status_code == 204

    @pytest.mark.django_db
    def test_delete_one_animal_not_found(self, client, animal_saved):
        response = client.delete('/animals/20/')

        assert response.status_code == 404
        assert response.json() == {'detail': 'Não encontrado.'}
