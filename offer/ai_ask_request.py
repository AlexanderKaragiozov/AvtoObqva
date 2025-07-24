import json

import requests

def query_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )


    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def run_ollama(make, model, year, horsepower):
    prompt = f"""
    Въз основа на следната информация за превозното средство:

    - Марка: {make}
    - Модел: {model}
    - Година: {year}
    - Конски сили: {horsepower}

    Предостави кратка и ясна информация само по следните 7 категории, без въвеждащ или заключителен текст:

    1. Надеждност
    2. Често срещани проблеми / Известни дефекти
    3. Трансмисия
    4. Въздействие върху околната среда
    5. Разход на гориво
    6. Безопасност
    7. Разходи за поддръжка
    ВЪРНИ МИ ИНФОРМАЦИЯТА НА БЪЛГАРСКИ ЕЗИК (ако има много сложни думи не ги превеждай)
    Всяка точка да бъде на НОВ РЕД
    Всяка точка да бъде маркирана с номер и заглавие, последвано от описанието ѝ. Използвай стегнат и информативен стил.
    """

    output = query_ollama(prompt)
    return output
