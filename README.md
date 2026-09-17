## AI Banking Assistant

REST API for learning the fundamentals of AI Engineering with Python,
FastAPI, and an LLM API.

### Initial setup

In PowerShell, from the project root:

```powershell
py -3.12 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

The `.env` file should contain local settings and must never be versioned.
