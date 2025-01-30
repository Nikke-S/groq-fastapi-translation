# Groq FastAPI Translation API

This is a **FastAPI-based translation API** that uses the **Groq API** to translate text into different languages.

## Features
- Fast and simple translation API  
- Uses Groq's **LLM models** for accurate translations  
- Deployable on **Google Colab, local machine, or cloud**  

---

## Installation & Setup  

### Clone the Repository
```sh
git clone https://github.com/Nikke-S/groq-fastapi-translation.git
cd groq-fastapi-translation
```

### Install Dependencies
```sh
pip install fastapi uvicorn python-dotenv requests
```

### Set Up API Key
- Create a `.env` file in the project folder  
- Add your **Groq API key** inside:
  ```env
  GROQ_API_KEY=your_api_key_here
  ```

### Run the FastAPI Server
```sh
uvicorn groq_api:app --host 0.0.0.0 --port 8000 --reload
```
The API will be available at:  
**http://127.0.0.1:8000/docs** (Swagger UI)  

---

## API Usage  

### Translate Text
**Endpoint:** `POST /translate/`  
**Example Request:**
```json
{
  "text": "Hello, how are you?",
  "target_language": "fr"
}
```
**Example Response:**
```json
{
  "translated_text": "Bonjour, comment ça va?"
}
```

---

## Deploying with Ngrok
If using **Google Colab**, expose the API online:
```python
from pyngrok import ngrok
public_url = ngrok.connect(8000, "http")
print(f"Public URL: {public_url}")
```

---

## License  
This project is **open-source** and available under the **MIT License**.

---

## Author  
**Nikke-S**  
GitHub: [Nikke-S](https://github.com/Nikke-S)
