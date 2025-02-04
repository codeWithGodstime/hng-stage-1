from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import math
import requests

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n: int) -> bool:
    if n <= 0:
        return False
    return n == sum(i for i in range(1, n) if n % i == 0)


def is_armstrong(n: int) -> bool:
    if n < 0:
        return False
    digits = [int(digit) for digit in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n


def get_fun_fact(n: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math", timeout=5)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return "Fun fact not available at the moment."
    return "Fun fact not available."


@app.get("/api/classify-number")
async def classify_number(
    number: int = Query(..., description="The number to classify"),
):
    properties = []

    if number < 0:
        return {
            "number": number,
            "is_prime": False, 
            "is_perfect": False,
            "properties": ["even" if number % 2 == 0 else "odd"],
            "digit_sum": sum(int(d) for d in str(abs(number))),
            "fun_fact": get_fun_fact(number),
        }

    if is_armstrong(number):
        properties.append("armstrong")

    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(number))),  # Fixed sum calculation
        "fun_fact": get_fun_fact(number),
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
