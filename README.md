## AI Banking Assistant

API REST de aprendizado para explorar fundamentos de AI Engineering com Python,
FastAPI e uma API de LLM.

### Configuração inicial

No PowerShell, a partir da raiz do projeto:

```powershell
py -3.12 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

O arquivo `.env` deve conter configurações locais e nunca deve ser versionado.
