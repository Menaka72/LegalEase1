from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ai_core.gemini_generator import GeminiDocumentGenerator
from utils import format_docx, format_pdf

router = APIRouter()
generator = GeminiDocumentGenerator()

class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str

class ExportRequest(BaseModel):
    text: str
    document_type: str

@router.post("/generate")
def generate_document(request: DocumentRequest):
    try:
        document = generator.generate_document(
            request.document_type,
            request.parties,
            request.terms,
            request.dates
        )
        return {"document": document}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/export/docx")
def export_docx(request: ExportRequest):
    return format_docx(request.text, request.document_type)

@router.post("/export/pdf")
def export_pdf_file(request: ExportRequest):
    return format_pdf(request.text, request.document_type)
