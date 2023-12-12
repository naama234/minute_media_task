**Make sure you have pytest and selenium installed in your project** -

`pip install pytest`

`pip install selenium`

**Bug report** -
1. The response of delete request is 500 - the delete not working as expected.  Found in - `test_delete_user`.

**Documentation - Test plan**
1. test_add_user:
    Create payload.
    Add the user with POST request.
    Excepted result -
    1. The status code of the response is 200.
    2. The response contain the expected data.
    Actual results:
    1. The status code of the response is 200.
    2. The response contain the expected data.


2. test_get_user:
   Create new user.
   Get the user with GET request.
   Excepted result -
    1. The status code of the response is 200.
    2. The response contain the expected data.
    Actual results:
    1. The status code of the response is 200.
    2. The response contain the expected data.

3. test_get_not_existing_user:
   Set invalid user id.
   Get the user with GET request.
   Excepted result -
    1. The status code of the response is 404.
    Actual results:
    1. The status code of the response is 404.

4. test_get_users():
    Create user.
    Get the user with GET request.
   Excepted result -
    1. The status code of the response is 200.
    2. The response contain the expected data.
    Actual results:
    1. The status code of the response is 200.
    2. The response contain the expected data.


5. test_edit_user():
   Create user.
   Edit the user with PUT request.
   Excepted result -
    1. The status code of the response is 200.
    2. The response contain the expected data.
       Actual results:
    1. The status code of the response is 200.
    2. The response contain the expected and updated data.



6. test_delete_user():
   Create user.
   Delete the user with DELETE request.
   Excepted result -
    1. The status code of the response is 200.
    2. The user should not exist.
       Actual results:
    1. The status code of the response is 404.
    2. The user still exist.
   

