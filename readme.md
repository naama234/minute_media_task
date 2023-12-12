**Make sure you have pytest and selenium installed in your project** -

`pip install pytest`

`pip install selenium`

**Bug report** -
backend test

1. Get user by id not working as expected, for all the id (existing and unexisting) we get "user not found" message. Found in - `test_get_user` 
2. The edit not working as expected, the name not updated. Found in `test_edit_user`
3. The id is not unique - we can create two items with the same id.

UI test

1. The following links not display in the list -
   "Transfers", "FanVoice", "The Switch", "EFL", "La Liga", "Serie A"


**Documentation - Test plan for backend**
1. add_user:
    Create payload.
    Add the user with POST request.
    Excepted result -
    1. The status code of the response is 200.
    2. The response contain the expected data.
    Actual results:
    1. The status code of the response is 200.
    2. The response contain the expected data.


2. get_user:
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
   


