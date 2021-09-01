## **Get One Todo**

Returns json data for one todo item

- **URL**

  /api/v1/todos/:id

- **Method:**

  `GET`

- **URL Params**

  **Required:**

  `id=[integer]`

- **Data Params**

  None

- **Success Response:**

  - **Code:** 200 <br />
    **Content:** ` { "id": 1, "uuid": "55dd9b2d-5bdf-4d4c-b9b7-73e83d94ddb2", "subject": "support for priorities +feature", "projects": ["feature"], "due": "2016-07-08", "completed": false, "completedDate": "", "archived": false, "isPriority": false, "notes": ["today iss day"] }`

    or

  - **Code:** 200 <br />
    **Content:** `{ "data": [] }`

<!-- - **Error Response:**

  - **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Todo doesn't exist" }` -->

## **Add One Todo**

Returns  add to json data for one todo item

- **URL**

  /api/v1/todos/

- **Method:**

  `POST`

- **URL Params**

- **Data Params**

  None

- **Success Response:**

  - **Code:** 201 <br />
    **Content:** `{ new_todo = {"id": id, "uuid": uuid, "subject": subject, "projects": projects, "due": due, "completed": completed,
    "completedDate": completedDate, "archived": archived, "isPriority": isPriority, "notes": notes} }'


or
- **Fail Response:**

- **Code:** 400 <br />
  **Content:** `{return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)}`

## **Update One Todo**

Returns update json data for one todo item or more

- **URL**

  /api/v1/todos/:id

- **Method:**

  `PATCH`

- **URL Params**

  **Required:**

  `id=[integer]`

- **Data Params**

  None

- **Success Response:**

  - **Code:** 200 <br />
    **Content:** ` {  }`

    or

  - **Code:** 200 <br />
    **Content:** `{ return Response({'message': 'updated completed'} }`

    or 

  - **Code:** 200 <br />
    **Content:** `{ return Response({'message': 'updated '} }`
    or
    - **Fail Response:**

  - **Code:** 400 <br />
    **Content:** `{return Response(serializer_complete.errors,status=status.HTTP_400_BAD_REQUEST) }`

    or
    - **Fail Response:**

  - **Code:** 400 <br />
    **Content:** `{return Response({}, status=statuHTTP_400_BAD_REQUEST)}`
    

  
## **Delete One Todo**

Returns delete json data for one todo item

- **URL**

  /api/v1/todos/:id

- **Method:**

  `DELETE`

- **URL Params**

  **Required:**

  `id=[integer]`

- **Data Params**

  None

- **Success Response:**

  - **Code:** 200 <br />
    **Content:** ` { }`

    or

  - **Code:** 200 <br />
    **Content:** `{return Response({"message": "Todo deleted"})}`
