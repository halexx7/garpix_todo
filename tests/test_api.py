import unittest

import requests

from todo.models.task_model import Task


class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/api"
    TASKS_URL = f"{API_URL}/task/"
    TEST_DAO = Task()
    ID = 7
    TASK_OBJ = {"id": ID, "title": "Internship at GARPIX", "content": "Complete test task"}
    NEW_TASK_OBJ = {
        "id": ID,
        "title": "I completed an internship at GARPIX",
        "content": "Successfully completed my internship and work at GARPIX",
    }

    def _get_each_task_url(self, id):
        return f"{self.TASKS_URL}{id}"

    # GET request to /api/task/ returns the details of all tasks
    def test_1_get_all_tasks(self):
        r = requests.get(self.TASKS_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 6)

    # POST request to /api/task to create a new task
    def test_2_add_new_task(self):
        r = requests.post(self.TASKS_URL, json=self.TASK_OBJ)
        self.assertEqual(r.status_code, 201)

    # GET request to /api/task/id returns the details of one task
    def test_3_get_new_task(self):
        r = requests.get(self._get_each_task_url(self.ID))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["title"], self.TASK_OBJ["title"])

    # PUT request to /api/task/id to update a existing task
    def test_4_update_existing_task(self):
        r = requests.put(self._get_each_task_url(self.ID), json=self.NEW_TASK_OBJ)
        self.assertEqual(r.status_code, 200)

    # GET request to /api/task/id returns the details of one task
    def test_5_get_new_task_after_update(self):
        r = requests.get(self._get_each_task_url(self.ID))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["title"], self.NEW_TASK_OBJ["title"])

    # DELETE request to /api/task/id to delete a existing task
    def test_6_delete_task(self):
        r = requests.delete(self._get_each_task_url(self.ID))
        self.assertEqual(r.status_code, 204)

    def test_7_get_new_task_after_delete(self):
        r = requests.delete(self._get_each_task_url(self.ID))
        self.assertEqual(r.status_code, 404)
