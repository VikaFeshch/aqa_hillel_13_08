
import pytest
from assertpy import assert_that

from lesson_24.data.add_pet import pet_data_list
from lesson_24.src.app import App


@pytest.mark.parametrize("pet_data", pet_data_list, ids=[f"pet-{pet['id']}" for pet in pet_data_list])
def test_create_and_get_pet(app_auth: App, pet_data):
    # Step 1: Get pet without id
    with pytest.raises(RuntimeError) as e:
        app_auth.pet.get_pet_by_id(pet_data["id"])
    # Step 2: Add pet
    response = app_auth.pet.add_pet(pet_data)
    assert_that(response).is_equal_to(pet_data)
    # Step 3: Get pet by id
    pet_id = pet_data["id"]
    response = app_auth.pet.get_pet_by_id(pet_id)
    assert_that(response).is_equal_to(pet_data)
