import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiDocumentGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is missing in .env")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def generate_document(self, document_type, parties, terms, dates):
        prompt = f"""
Create a professional draft legal document.

Document Type: {document_type}
Parties: {parties}
Terms: {terms}
Effective Date: {dates}

Use clear headings and formal language.
Include the document title, parties, effective date, terms and conditions,
responsibilities where appropriate, termination where appropriate, and
signature placeholders.

Important: This is an AI-generated draft for informational purposes and
should be reviewed by a qualified legal professional before use.
"""

        response = self.model.generate_content(prompt)
        return response.text
