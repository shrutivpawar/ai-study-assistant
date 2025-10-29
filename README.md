# AI Study Assistant

Lightweight Flask app that provides study assistance (summaries, explanations, quizzes) using the OpenAI API.

## Features
- Summarize text into short bullet points
- Explain concepts at different education levels
- Generate short quizzes with answer keys

## Prerequisites
- Python 3.8+ (this project was tested with Python 3.13)
- An OpenAI API key

## Quick setup (Windows / PowerShell)

1. Clone the repo (if you haven't already):

```powershell
git clone https://github.com/shrutivpawar/ai-study-assistant.git
cd "ai-study-assistant"
```

2. (Optional but recommended) Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Configure your OpenAI API key:

Create a `.env` file in the project root with this content (do NOT commit the real key):

```
OPENAI_API_KEY=sk-REPLACE_WITH_YOUR_REAL_KEY
```

The repository already includes `.gitignore` which ignores `.env`.

Alternatively, set the key in the current PowerShell session for quick testing:

```powershell
$env:OPENAI_API_KEY = "sk-REPLACE_WITH_YOUR_REAL_KEY"
python .\app.py
```

5. Run the app (development server):

```powershell
python .\app.py
# By default Flask serves on http://127.0.0.1:5000
```

## Endpoints
- `GET /` — index page
- `POST /api/summarize` — JSON {"text":"..."}
- `POST /api/explain` — JSON {"text":"...", "level":"highschool"}
- `POST /api/quiz` — JSON {"text":"...", "count":3}

Responses are JSON with `result` on success or `error` on failure.

## Security
- Keep your OpenAI API key private. Do not commit `.env` to source control.
- Rotate your key immediately if you believe it was exposed. (Because keys were pasted during local dev, consider regenerating.)

## Troubleshooting
- If the app prints a warning about `OPENAI_API_KEY` being a placeholder, replace it with a real key in `.env` or set the env var.
- If you see `ModuleNotFoundError: No module named 'dotenv'`, run `pip install python-dotenv` or `pip install -r requirements.txt`.

## Contributing
Contributions welcome — open a PR with feature requests or fixes.

## License
This project does not include an explicit license file. Add a LICENSE if you want to set terms.
