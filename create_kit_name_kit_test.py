import sender_stand_request
import data
from data import kit_body_1


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

def test_create_kit_1_letter():
    new_kit_body = get_kit_body(kit_body_1)
    positive_assert(new_kit_body)

def test_create_kit_511_letter():
    new_kit_body = get_kit_body('kit_body_2')
    positive_assert(new_kit_body)

def test_create_kit_0_a_la_permitida_letter():
    new_kit_body = get_kit_body('kit_body_3')
    negative_assert_code_400(new_kit_body)

def test_create_kit_512_letter():
    new_kit_body = get_kit_body('kit_body_4')
    negative_assert_code_400(new_kit_body)

def test_create_kit_permite_caracter_especial_letter():
    new_kit_body = get_kit_body('kit_body_5')
    positive_assert(new_kit_body)

def test_create_kit__permite_espacios_letter():
    new_kit_body = get_kit_body('kit_body_6')
    positive_assert(new_kit_body)

def test_create_kit_permite_numeros_letter():
    new_kit_body = get_kit_body('kit_body_7')
    positive_assert(new_kit_body)

def test_create_kit_error_name_letter():
    new_kit_body = get_kit_body('kit_body_8')
    negative_assert_code_400(new_kit_body)

def test_create_kit_parametro_diferente_letter():
    new_kit_body = get_kit_body('kit_body_9')
    negative_assert_code_400(new_kit_body)