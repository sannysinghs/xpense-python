import PyPDF2
import tabula
import re
import regx_utils as patterns

def pdf_to_rows_with_miner(file): 
    rows = []
    result = tabula.read_pdf(file, pages='all', stream=True)
    tabula.convert_into(file, "iplmatch.csv", output_format="csv", pages='all')
    return len(result)

def pdf_to_rows(pdf_path):
    rows = []
    with open(pdf_path, 'rb') as file:

        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            rows.extend(text.split("\n"))

    return rows

date_len = 6
def get_trans_details(title, body, body2): 
    result = {}
    
    result['date'] = title[:date_len]
    result['body'] = body[:body.lower().find("singapore")]
    
    match = re.search(
        pattern= re.compile(patterns.credit_trans), string=body+ "" +body2)
    
    result['amount'] = match.group() if match else "NA"
    return result


if __name__ == "__main__":
    pdf_path = "/Users/sanny/Downloads/eStatement_49180.94873817442.pdf"  # Replace with the path to your PDF file
    rows = pdf_to_rows(pdf_path)
    print(rows)
    trans = [] 


    pattern_card = re.compile(patterns.card_trans_regx)
    for i, row in enumerate(rows, start=1):
       if re.match(pattern_card, row): 
           trans.append(get_trans_details(row, body= rows[i], body2= rows[i+1]))
    
    p_paynow = re.compile(patterns.paynow_trans)
    for i, row in enumerate(rows, start=1):
       if re.match(p_paynow, row): 
           trans.append(get_trans_details(row, body= rows[i], body2= rows[i+1]))
