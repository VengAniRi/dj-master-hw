import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT


# def test_example_prime():
#     assert True, "Just test example"
#
#
# def test_example():
#     assert False, "Just test example"

# @pytest.mark.parametrize(
#     ["unit_price", "expected_status"],
#     (  ("400", HTTP_201_CREATED),
#        ("-100", HTTP_400_BAD_REQUEST),
#        ("100000000", HTTP_400_BAD_REQUEST),))
# @pytest.mark.django_db
# def test_product_create_validation(unit_price, expected_status):
#     client = APIClient()
#     url = reverse("products-list")
#     product_payload = {  "name": "Test",  "unit_price": unit_price,}
#     resp = client.post(url, product_payload)
#     assert resp.status_code == expected_status


from students.models import Course


@pytest.mark.django_db
def test_courses_get_one(api_client, course_factory):
    course = course_factory()
    url = reverse("courses-detail", args=(course.id, ))
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json['id'] == course.id
    assert resp_json['name'] == course.name


@pytest.mark.django_db
def test_courses_get_list(api_client, course_factory):
    courses = course_factory(_quantity=2)
    url = reverse("courses-list")
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == len(courses)
    generated_ids = [course.id for course in courses]
    assert generated_ids == [course["id"] for course in resp_json]


@pytest.mark.django_db
def test_courses_list_filter_id(api_client, course_factory):
    courses = course_factory(_quantity=2)
    url = reverse("courses-list")
    resp = api_client.get(url, {'id': courses[1].id})
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 1
    assert resp_json[0]['id'] == courses[1].id
    assert resp_json[0]['name'] == courses[1].name


@pytest.mark.django_db
def test_courses_list_filter_name(api_client):
    courses = Course.objects.bulk_create([
        Course(name="Phys 1"),
        Course(name="Phys 2"),
    ])
    url = reverse("courses-list")
    resp = api_client.get(url, {'name': courses[1].name})
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 1
    assert resp_json[0]['id'] == courses[1].id
    assert resp_json[0]['name'] == courses[1].name


@pytest.mark.django_db
def test_courses_create(api_client):
    course_payload = {
        'name': 'Python',
        'students': [],
    }
    url = reverse("courses-list")
    resp = api_client.post(url, course_payload)
    assert resp.status_code == HTTP_201_CREATED


@pytest.mark.django_db
def test_courses_update(api_client, course_factory):
    course = course_factory()
    new_name = 'New ' + course.name
    course_payload = {
        'name': new_name
    }
    url = reverse("courses-detail", args=(course.id, ))
    resp = api_client.patch(url, course_payload)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json["name"] == new_name


@pytest.mark.django_db
def test_courses_destroy(api_client, course_factory):
    courses = course_factory(_quantity=4)
    url_list = reverse("courses-list")
    resp = api_client.get(url_list)
    assert resp.status_code == HTTP_200_OK
    len_before_delete = len(resp.json())

    url_detail = reverse("courses-detail", args=(courses[2].id, ))
    resp = api_client.delete(url_detail)
    assert resp.status_code == HTTP_204_NO_CONTENT

    resp = api_client.get(url_list)
    assert resp.status_code == HTTP_200_OK
    len_after_delete = len(resp.json())

    assert len_before_delete == len_after_delete + 1
    resp_json = resp.json()
    assert courses[2].id not in [course["id"] for course in resp_json]
