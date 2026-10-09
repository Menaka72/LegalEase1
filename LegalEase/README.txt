LEGALEASE - SIMPLE VERSION

1. Open this folder in VS Code.

2. Open Terminal and run:
   pip install -r requirements.txt

3. Rename .env.example to .env

4. Open .env and replace:
   YOUR_GEMINI_API_KEY_HERE
   with your Gemini API key.

5. Start backend in Terminal 1:
   uvicorn main:app --reload

6. Open another Terminal 2:
   streamlit run app.py

7. The Streamlit page will open in your browser.

Project flow:
Streamlit -> FastAPI -> Gemini -> Generated Document -> Edit -> TXT/DOCX/PDF

Note:
The AI-generated legal document is a draft and should be reviewed by a qualified legal professional before use.
