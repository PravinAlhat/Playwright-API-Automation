class Variables:
    ENDPOINT_URL = "https://reqres.in"
    HEADERS = {
            "content-type" : "application/json",
            "x-api-key" : "reqres-free-v1"
        }
    LIST_USER_ENDPOINT = "/api/users?page=2"
    LIST_SINGLE_USER = "/api/users/id"
    CREATE_USER = "/api/users"
    DELETE_USER_ENDPOINT = "/api/users/id"
    CREATEUSER_NAME = "Jim"
    CREATEUSER_JOB = "Wade"
    CREATEUSER_STATUS_CODE = 201
    LIST_USER_ID = "2"
    DELETE_USER_ID = "2"
    LIST_SINGLE_INVALID_USER = "/api/unknown/23"
    INVALID_USER_STATUS_CODE = 404