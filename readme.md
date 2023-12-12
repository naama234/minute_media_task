**Make sure you have pytest and selenium installed in your project** -

`pip install pytest`

`pip install selenium`

**Bug report UI test** -

1. The following links not display in the list -
   "Transfers", "FanVoice", "The Switch", "EFL", "La Liga", "Serie A"

**Bug report backend tests** -

1. Get user by id not working as expected, for all the ids (existing and unexisting) we get "user not found" message. Steps in - `test_get_user`
2. The edit not working as expected, the name not updated. Steps in `test_edit_user`
3. The id is not unique - we can create two items with the same id. Steps in `test_add_us_with_same_id`


**Backend Documentation - Test plan**

test_add_user file

1. test_add_user:

   Add a user with POST request.

   **Excepted result:**

   a.The status code of the response is 200.

   b.The response contain the expected data.

   **Actual results:**

   a.The status code of the response is 200.

   b.The response contain the expected data.



2. test_add_user_with_long_name:

   Add user with long name with POST request.

   **Excepted result:**

   a.The status code of the response is 200.

   b.The response contain the expected data.

   **Actual results:**

   a.The status code of the response is 200.

   b.The response contain the expected data.


3. test_add_user_with_long_id:

   Add user with long id with POST request.

   **Excepted result:**

   a.The status code of the response is 200.

   b.The response contain the expected data.

   **Actual results:**

   a.The status code of the response is 200.

   b.The response contain the expected data.


4. test_add_user_with_empty_name:

   Add user with empty name with POST request.

   **Excepted result:**

   a.The status code of the response is 400.

   **Actual results:**

   a.The status code of the response is 200.


5.  test_add_user_with_empty_id:

    Add user with empty id with POST request.

    **Excepted result:**

    a.The status code of the response is 400.

    **Actual results:**

    a.The status code of the response is 200.


6. test_add_user_with_empty_id_and_empty_name:
   Add user with empty name and id with POST request.

   **Excepted result:**

   a.The status code of the response is 400.

   **Actual results:**

   a.The status code of the response is 200.


7. test_add_us_with_same_id:

   Add the user with POST request and then add the same user with the post request.

   **Excepted result:**

   a.The status code of the response is 400.

   **Actual results:**

   a.The status code of the response is 200.

test edit user file -

1. test_edit_user

   1.Add a sample user with the provided sample_user fixture.

   2.Prepare payload for updating the user's name.

   3.Send a PUT request to edit the user using the prepared payload.

   **Excepted result:**

   a.The status code of the response is 200.

   b. The response contain the expected data.

   c. Get the user and make sure the name was updated.

   **Actual results:**

   a.The status code of the response is 404.

   b. The response contain the expected data.

   c. The name not updated.


2. test_edit_unexisting_user:

   1. Update username with id that not exist.

   **Excepted result:**

   a.The status code of the response is 404.

   **Actual results:**

   a.The status code of the response is 404.

test_get_users file

1. test_get_users -

   a. Create simple user

   b. Get all users using GET request.

   **Excepted result:**

   a.The status code of the response is 200.

   b. Check response body is a list.

   c. Search the user we created in the list.

   **Actual result:**

   a.The status code of the response is 200.

   b. The response body is a list.

   c. The user in the list.


test_delete_user file -
1. test_delete_user -
   a. Create simple user

   b. delete the user using DELETE request.

   **Excepted result:**

   a.The status code of the response is 200.

   b. Check response body not contain the deleted user.

   c. Get the deleted user and make sure it not exist.

   **Actual result:**

   a.The status code of the response is 200.

   b. The response body not contain the deleted user.

   c. Can nor test this case because there is a bug in the GET request.

   2. test_delete_unexisting_user -

      a. Delete user with invalid id using DELETE request.

      **Excepted result:**
      a. The status code of the response is 500.

      **Excepted result:**

      a.The status code of the response is 500.
   
   

   3. test_delete_with_long_id -

      a. Delete user with long id using DELETE request.

      **Excepted result:**

      a.The status code of the response is 200.
      
      b. Check response body not contain the deleted user.
      
      c. Get the deleted user and make sure it not exist.
      
      **Actual result:**
      
      a.The status code of the response is 200.
      
      b. The response body not contain the deleted user.
      
      c. Can not test this case because there is a bug in the GET request.


test_get_user file -
1. test_get_user

    a. Create user.
    
    b. Get the user with GET request.

    **Excepted result:**

    a.The status code of the response is 200. 

   b. The response contain the expected data.

    **Actual result:**

    a.The status code of the response is 404. 
   
   b. Can not test this case because there is a bug in the GET request.


2. test_get_not_existing_user -

   a. Get the user with invalid id.

   **Excepted result:**

   a.The status code of the response is 404.

   **Actual result:**

   a.The status code of the response is 404.







