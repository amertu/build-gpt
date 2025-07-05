from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse

from parsers.maven_parser import parse_maven_log
from parsers.npm_parser import parse_npm_log
from context.github_context import get_code_context
from gpt_service import analyze_with_gpt

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Build-GPT service running"}


@app.post("/analyze-log")
async def analyze_log(
    file: UploadFile = File(...),
    type: str = Form(...)
):
    if type not in {"maven", "npm"}:
        raise HTTPException(status_code=400, detail="Unsupported log type")

    log_text = await file.read()
    log_text = log_text.decode("utf-8")

    # Step 1: Parse error from logs
    if type == "maven":
        error_info = parse_maven_log(log_text)
    else:
        error_info = parse_npm_log(log_text)

    if not error_info:
        raise HTTPException(status_code=422, detail="Could not parse error from log")

    return JSONResponse(content={"error": error_info})

