import playwright
import pytest
from utility.utils import Variables as V
from utility.custom_utils import payload as get_data
from utility.custom_utils import *
import unittest
from utility.logger import custom_logger as cl
import logging
from utility.custom_utils import move_dir

@pytest.mark.usefixtures("OneTimeSetup", "get_context")
class TestUserAPI(unittest.TestCase):
    log = cl(loglevel=logging.DEBUG)

    @pytest.fixture(autouse=True)
    def object_setup(self, OneTimeSetup, get_context):
        self.url = OneTimeSetup
        self.context = get_context

    def test_list_user(self):
        try:
            response = list_user(self.context, self.url, V.LIST_USER_ENDPOINT)
            assert response.status == 200
            assert response.json()["data"][1]["id"] == 8
            self.log.info("Users are listed successfully")
        except:
            self.log.error("Users are not listed and test is failed")
            raise Exception

    def test_single_user(self):
        try:
            response = list_single_user(self.context, self.url, V.LIST_SINGLE_USER, V.LIST_USER_ID)
            assert response.status == 200
            self.log.info(f"Single user with ID {V.LIST_USER_ID} is successfully fetched and listed")
        except:
            self.log.error(f"User with ID {V.LIST_USER_ID} is not listed and test is failed")

    def test_create_user(self):
        try:
            response = create_user(self.context, self.url, V.CREATE_USER, V.CREATEUSER_NAME, V.CREATEUSER_JOB)
            assert response.status == V.CREATEUSER_STATUS_CODE
            self.log.info(f"User is successfully created with Name '{V.CREATEUSER_NAME}' and Job '{V.CREATEUSER_JOB}'")
        except:
            self.log.error(f"User is not created with Name {V.CREATEUSER_NAME} and Job {V.CREATEUSER_JOB} and test is failed")

    def test_delete_user(self):
        try:
            response = delete_user(self.context, self.url, V.DELETE_USER_ENDPOINT, V.DELETE_USER_ID)
            self.log.info(f"User with ID {V.DELETE_USER_ID} is successfully deleted")
        except:
            self.log.error(f"User with ID is not deleted and test is failed")

    def test_single_user_not_found(self):
        try:
            response = single_invalid_user(self.context, self.url, V.LIST_SINGLE_INVALID_USER)
            assert response.status == V.INVALID_USER_STATUS_CODE
            self.log.info("Invalid user")
        except:
            self.log.error("Test is failed")
            
            
