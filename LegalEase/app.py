import streamlit as st
import requests

st.set_page_config(page_title="LegalEase", page_icon="⚖️", layout="centered")

st.title("⚖️ LegalEase")
st.write("AI-Powered Legal Document Generator")
st.divider()

document_type = st.selectbox(
    "Document Type",
    ["Employment Contract", "NDA", "Lease Agreement", "Agreement", "Contract", "Employment Offer Letter"]
)

parties = st.text_area("Parties Involved", placeholder="Example: John Doe (Employee), ABC Company (Employer)")
terms = st.text_area("Terms & Conditions", placeholder="Example: Salary is paid monthly; Confidentiality must be maintained; Either party may terminate with 15 days notice")
dates = st.date_input("Effective Date")

if st.button("Generate Document"):
    if not parties or not terms:
        st.warning("Please enter the parties and terms.")
    else:
        data = {
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "dates": str(dates)
        }

        try:
            response = requests.post("http://127.0.0.1:8000/generate", json=data)

            if response.status_code == 200:
                result = response.json()["document"]
                st.session_state["document"] = result
            else:
                st.error(response.json().get("detail", "Something went wrong."))
        except requests.exceptions.ConnectionError:
            st.error("Backend is not running. Start main.py first.")

if "document" in st.session_state:
    st.subheader("Generated Document")

    edited_document = st.text_area(
        "Edit Document",
        value=st.session_state["document"],
        height=450
    )

    st.session_state["document"] = edited_document

    st.download_button(
        "Download TXT",
        edited_document,
        file_name="legal_document.txt",
        mime="text/plain"
    )

    try:
        docx_response = requests.post(
            "http://127.0.0.1:8000/export/docx",
            json={"text": edited_document, "document_type": document_type}
        )
        if docx_response.status_code == 200:
            st.download_button(
                "Download DOCX",
                docx_response.content,
                file_name="legal_document.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        pdf_response = requests.post(
            "http://127.0.0.1:8000/export/pdf",
            json={"text": edited_document, "document_type": document_type}
        )
        if pdf_response.status_code == 200:
            st.download_button(
                "Download PDF",
                pdf_response.content,
                file_name="legal_document.pdf",
                mime="application/pdf"
            )
    except requests.exceptions.ConnectionError:
        pass
