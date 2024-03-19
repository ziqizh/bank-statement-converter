import fitz  # PyMuPDF
import json

def load_keywords():
    keywords = []
    with open('keywords.json', 'r') as file:
        data = json.load(file)
        keywords += data['locations'] + data['banks']

    with open('config.json', 'r') as file:
        data = json.load(file)
        keywords += data['names'] + data['addresses'] + data['accounts']
    return keywords


def redact_text_in_pdf(input_pdf_path, output_pdf_path, keywords):
    # Open the PDF file
    doc = fitz.open(input_pdf_path)
    
    for page in doc:
        # Search for the text on each page
        for text_to_redact in keywords:
            text_instances = page.search_for(text_to_redact)
        
            # Apply redaction (add a redaction annotation for each instance found)
            for inst in text_instances:
                page.add_redact_annot(inst, text="")  # Leaving text argument empty to just remove text
            
        # Apply the redaction, effectively removing the text
        page.apply_redactions()

    # Save the redacted document
    doc.save(output_pdf_path)
    doc.close()

# Example usage
input_pdf = "samples/sample_statement.pdf"
output_pdf = "samples/sample_statement_redacted.pdf"
keywords = load_keywords()

redact_text_in_pdf(input_pdf, output_pdf, keywords)