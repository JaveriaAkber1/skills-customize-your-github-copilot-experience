"""Starter application for the FastAPI REST API assignment.

Install dependencies with:
    pip install fastapi uvicorn

Run the API with:
    uvicorn starter-code:app --reload

Then open http://127.0.0.1:8000/docs to explore the API.
"""

from fastapi import FastAPI

app = FastAPI(title="Items API")


items = []


@app.get("/health")
def health_check():
    """Return a response that confirms the API is running."""
    pass


@app.get("/items")
def list_items():
    """Return every item in the collection."""
    pass


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Return one item by its ID."""
    pass


@app.post("/items")
def create_item(item: dict):
    """Create and return a new item."""
    pass


@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    """Update and return an existing item."""
    pass
