#  Lie Detector AI (Fact Checker)

A simple web app that uses **Flask** (Python backend) and **OpenAI API** to verify whether a statement is **True, False, or Unverifiable**.
The app has a **frontend** (HTML/JS) and a **Flask backend** that communicates with the OpenAI API for fact-checking.


## 📂 Project Structure

```
project-root/
│
├── backend/
│   └── app.py              # Flask backend
│
├── frontend/
│   ├── index.html          # Web UI
│   └── ...                 # Any JS/CSS files
│
├── .env                    # Environment variables (OpenAI API Key)
├── requirements.txt        # Python dependencies
└── README.md               # This file


## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/cloudcaptain9/factcheck-app.git
cd factcheck-ai/backend
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file in the **backend** folder:


OPENAI_API_KEY=your_openai_api_key_here




## ▶️ Running the App

### Start the Flask server

```bash
python app.py


This starts the backend at **[http://localhost:8000](http://localhost:8000)**.

### Access the frontend

Open your browser and go to:
 [http://localhost:8000](http://localhost:8000)



## 📡 API Endpoints

### `POST /factcheck`

**Request body:**

```json
{
  "claim": "The Earth is flat."
}
```

**Response:

```json
{
  "result": {
    "verdict": "False",
    "reason": "Scientific consensus and evidence confirm the Earth is round."
  }
}
```

---
## creat your own dockerfile

## 🐳 Docker (Optional)

Build and run with Docker:

```bash
# Build image
docker build -t lie-detector .

# Run container
docker run -d -p 8000:8000 --name lie-detector-app lie-detector




## ✅ Features

* Fact-checks claims using OpenAI GPT models
* Returns structured JSON (`True/False/Unverifiable`)
* Simple Flask API + frontend
* Docker support for easy deployment



