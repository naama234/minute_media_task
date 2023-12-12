**Make sure you have pytest and selenium installed in your project** -

`pip install pytest`

`pip install selenium`

**Bug report** -

backend test

1. Get user by id not working as expected, for all the id (existing and unexisting) we get "user not found" message. Found in - `test_get_user` 
2. The edit not working as expected, the name not updated. Found in `test_edit_user`
3. The id is not unique - we can create two items with the same id. Found in `test_add_us_with_same_id`

UI test

1. The following links not display in the list -
   "Transfers", "FanVoice", "The Switch", "EFL", "La Liga", "Serie A"


**Backend Documentation - Test plan**

1. test_add_user:

    Add the user with POST request.
   
    Excepted result -

    a.The status code of the response is 200.

    b.The response contain the expected data. 
    
    Actual results:

    a.The status code of the response is 200.
    
    b.The response contain the expected data.



2. test_add_user_with_long_name:

    Add user with long name with POST request.
   
    Excepted result -

    a.The status code of the response is 200.

    b.The response contain the expected data. 
    
    Actual results:

    a.The status code of the response is 200.
    
    b.The response contain the expected data.


3. test_add_user_with_long_id:

    Add user with long id POST request.
   
    Excepted result -

    a.The status code of the response is 200.

    b.The response contain the expected data. 
    
    Actual results:

    a.The status code of the response is 200.
    
    b.The response contain the expected data.


4. test_add_user_with_empty_name:   

   Add user with empty name with POST request.

   Excepted result -

   a.The status code of the response is 500.

   Actual results:

   a.The status code of the response is 200.


5.  test_add_user_with_empty_id:

    Add user with empty id with POST request.
    
    Excepted result -
    
    a.The status code of the response is 500.
    
    Actual results:
    
    a.The status code of the response is 200.


6. test_add_user_with_empty_id_and_empty_name:
   Add user with empty name and id with POST request.

   Excepted result -

   a.The status code of the response is 500.

   Actual results:

   a.The status code of the response is 200.


7. test_add_us_with_same_id:

   Add the user with POST request and then add the same user with the post request. 

   Excepted result -

   a.The status code of the response is 409.

   Actual results:

   a.The status code of the response is 200.

test edit user file -

1. test_edit_user 
    1.Add a sample user with the provided sample_user fixture.

    2.Prepare payload for updating the user's name. 

   3. Send a PUT request to edit the user using the prepared payload.
   Excepted result -

   a.The status code of the response is 200. 
    
    b. The response contain the expected data.

    c.  The name of the user with ID USER_ID should be UPDATED_NAME

   Actual results:

   a.The status code of the response is 200.   

    b. The response contain the expected data.

   c.  The name of the user with ID USER_ID should be UPDATED_NAME
    










