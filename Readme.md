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

