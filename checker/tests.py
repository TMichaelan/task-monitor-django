# pylint: disable=unused-argument, too-many-lines, line-too-long
import pytest
from rest_framework import status


@pytest.mark.django_db
def test_task_open(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/123/")
    expected_response = {
        "id": 123,
        "status": "open",
        "answer_time": 1440,
        "date_created": "2024-05-22T08:30:16",
        "due_date": "2024-05-23T08:30:16",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db
def test_task_scheduled(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/125/")
    expected_response = {
        "id": 125,
        "status": "scheduled",
        "answer_time": 1440,
        "date_created": "2024-05-22T08:21:10",
        "due_date": "2024-05-23T08:21:10",
        "outcome": "authentic",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db
def test_task_scheduled_fake(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/126/")
    expected_response = {
        "id": 126,
        "status": "scheduled",
        "answer_time": 120,
        "date_created": "2024-05-22T08:18:44",
        "due_date": "2024-05-22T10:18:44",
        "outcome": "fake",
        "fake_outcome_reason": "inside-label",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db
def test_task_in_progress(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/127/")
    expected_response = {
        "id": 127,
        "status": "in-progress",
        "answer_time": 1440,
        "date_created": "2024-05-22T07:57:07",
        "due_date": "2024-05-23T07:57:07",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response
    assert "fake_outcome_reason" not in response.data


@pytest.mark.django_db
def test_task_update_needed(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/128/")
    expected_response = {
        "id": 128,
        "status": "update-needed",
        "answer_time": 120,
        "date_created": "2024-05-22T07:15:34",
        "due_date": "2024-05-22T09:15:34",
        "photos_to_resubmit": "hardware-engravings, inside-label, serial-number, made-in-label",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response
    assert "fake_outcome_reason" not in response.data


@pytest.mark.django_db
def test_task_closed(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/137/")
    expected_response = {
        "id": 137,
        "status": "closed",
        "answer_time": 30,
        "date_created": "2024-05-22T02:33:53",
        "due_date": "2024-05-22T03:03:53",
        "outcome": "authentic",
        "date_closed": "2024-05-22T02:57:59",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db
def test_task_not_found(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/999/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == {"error": "Task not found"}


@pytest.mark.django_db
def test_task_not_authenticated(client, mock_task_data):
    response = client.get("/api/checker/task/123/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_task_123(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/123/")
    expected_response = {
        "id": 123,
        "status": "open",
        "answer_time": 1440,
        "date_created": "2024-05-22T08:30:16",
        "due_date": "2024-05-23T08:30:16",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db
def test_task_124(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/124/")
    expected_response = {
        "id": 124,
        "status": "open",
        "answer_time": 1440,
        "date_created": "2024-05-22T08:26:31",
        "due_date": "2024-05-23T08:26:31",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db
def test_task_129(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/129/")
    expected_response = {
        "id": 129,
        "status": "in-progress",
        "answer_time": 1440,
        "date_created": "2024-05-22T07:10:11",
        "due_date": "2024-05-23T07:10:11",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response
    assert "fake_outcome_reason" not in response.data


@pytest.mark.django_db
def test_task_130(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/130/")
    expected_response = {
        "id": 130,
        "status": "in-progress",
        "answer_time": 1440,
        "date_created": "2024-05-22T07:08:23",
        "due_date": "2024-05-23T07:08:23",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response
    assert "fake_outcome_reason" not in response.data


@pytest.mark.django_db
def test_task_131(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/131/")
    expected_response = {
        "id": 131,
        "status": "update-needed",
        "answer_time": 1440,
        "date_created": "2024-05-22T06:11:25",
        "due_date": "2024-05-23T06:11:25",
        "photos_to_resubmit": "brand-logo, inside-label, zipper-head-front, zipper-head-back, qr-code-label",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response
    assert "fake_outcome_reason" not in response.data


@pytest.mark.django_db
def test_task_134(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/134/")
    expected_response = {
        "id": 134,
        "status": "scheduled",
        "answer_time": 720,
        "date_created": "2024-05-22T05:37:29",
        "due_date": "2024-05-22T17:37:29",
        "outcome": "authentic",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response
    assert "fake_outcome_reason" not in response.data


@pytest.mark.django_db
def test_task_135(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/135/")
    expected_response = {
        "id": 135,
        "status": "scheduled",
        "answer_time": 720,
        "date_created": "2024-05-22T05:37:10",
        "due_date": "2024-05-22T17:37:10",
        "outcome": "fake",
        "fake_outcome_reason": "serial-number",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db
def test_task_139(auth_client, mock_task_data):
    response = auth_client.get("/api/checker/task/139/")
    expected_response = {
        "id": 139,
        "status": "closed",
        "answer_time": 1440,
        "date_created": "2024-05-22T02:10:50",
        "due_date": "2024-05-23T02:10:50",
        "outcome": "UTV",
        "fake_outcome_reason": "unknown",
        "date_closed": "2024-05-22T05:39:43",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response
