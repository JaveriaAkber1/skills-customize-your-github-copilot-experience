# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice defining routes, working with JSON data, and validating requests with Pydantic models.

## 📝 Tasks

### 🛠️ Complete the Health Check Route

#### Description
Run the starter application and complete the health check endpoint so a client can confirm that the API is available.

#### Requirements
Completed program should:

- Start with Uvicorn using the command shown in the starter code.
- Return a successful response from `GET /health`.
- Return a JSON object with the key `status` and the value `"ok"`.

### 🛠️ Build the Items API

#### Description
Create endpoints for a small in-memory collection of items. Each item should have an integer ID, a name, and a description.

#### Requirements
Completed program should:

- Return all items from `GET /items`.
- Return one item from `GET /items/{item_id}` and return HTTP 404 when the ID does not exist.
- Create an item with `POST /items` and return the newly created item as JSON.
- Assign each new item a unique integer ID.

### 🛠️ Add Validation and Updates

#### Description
Use Pydantic models to validate item data and add an endpoint that updates an existing item.

#### Requirements
Completed program should:

- Require a non-empty item name and a description for new items.
- Reject invalid request data with FastAPI's validation response.
- Update an existing item with `PUT /items/{item_id}`.
- Return HTTP 404 when an update targets an unknown ID.

For an optional stretch goal, add `DELETE /items/{item_id}` and return an appropriate response when the item is removed or does not exist.
