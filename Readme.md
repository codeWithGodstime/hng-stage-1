# Testing Number Classification API

## Overview
An API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Requirements
- Python 3.8+
- FastAPI
- requests

## Installation
1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/number-classification-api.git
    cd number-classification-api
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run the Server
    ```sh
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```