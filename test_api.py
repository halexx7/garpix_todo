import re
import unittest
import requests
from requests import status_codes

from main import TaskDAO


class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/api"
    TASKS_URL = f"{API_URL}/task/"
    TEST_DAO = TaskDAO()
    TASK_OBJ = {
        "id": 6,
        "title":"Internship at GARPIX", 
        "content": "Complete test task",
        "done": False
        }
    NEW_TASK_OBJ = {
        "id": 6,
        "title": "I completed an internship at GARPIX", 
        "content": "Successfully completed my internship and work at GARPIX",
        "done": False
    }

    def _get_each_task_url(self, id):
        return f"{ApiTest.TASKS_URL}{id}"

    # GET request to /api/task/ returns the details of all tasks
    def test_1_get_all_tasks(self):
        r = requests.get(ApiTest.TASKS_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 5)


    # POST request to /api/task to create a new task
    def test_2_add_new_task(self):
        r = requests.post(ApiTest.TASKS_URL, json=ApiTest.TASK_OBJ)
        self.assertEqual(r.status_code, 201)


    # GET request to /api/task/id returns the details of one task
    def test_3_get_new_task(self):
        id = 6
        r = requests.get(self._get_each_task_url(id))
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual(r.json(), ApiTest.TASK_OBJ)


    # PUT request to /api/task/id to update a existing task
    def test_4_update_existing_task(self):
        id = 6
        r = requests.put(self._get_each_task_url(id), json=ApiTest.NEW_TASK_OBJ)
        self.assertEqual(r.status_code, 200)


    # GET request to /api/task/id returns the details of one task
    def test_5_get_new_task_after_update(self):
        id = 6
        r = requests.get(self._get_each_task_url(id))
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual(r.json(), ApiTest.NEW_TASK_OBJ)


    # DELETE request to /api/task/id to delete a existing task
    def test_6_delete_task(self):
        id = 6
        r = requests.delete(self._get_each_task_url(id))
        self.assertEqual(r.status_code, 204)
    

    def test_7_get_new_task_after_delete(self):
        id = 6
        r = requests.delete(self._get_each_task_url(id))
        self.assertEqual(r.status_code, 404)


        # r = requests.get("http://127.0.0.1:5000/api/task/8")
