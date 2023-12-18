from py_pdf_parser.loaders import load_file
import regx_utils


def clean_up(raw_str):
    return raw_str.replace(",", "")


def get_trans_records(file):
    document = load_file(file)
    elements = document.elements.filter_by_regex(regex=regx_utils.date_pattern)
    total_balance = 0
    result = []
    treatments = {
        "one bonus interest": {
            "start_index": 1,
            "desc_index": 0
        },
        "interest credit": {
            "start_index": 1,
            "desc_index": 0
        }
    }
    initial_balance_filter = "balance b/f"

    for i, element in enumerate(elements):
        r_date = element.text()
        row = document.elements.to_the_right_of(element)

        if len(row.filter_by_text_equal(initial_balance_filter)) > 0:
            total_balance = float(clean_up(row[1].text()))

        if len(row) > 2:
            try:
                col_after_date = row[0].text().lower()
                start_index = 0 if col_after_date not in treatments else treatments[col_after_date]["start_index"]

                r_amount = float(clean_up(row[start_index].text()))
                r_balance = float(clean_up(row[start_index + 1].text()))
                r_desc = ""

                if len(row) > start_index + 2:
                    r_desc = row[start_index + 2].text()

                if col_after_date in treatments:
                    r_desc = row[treatments[col_after_date]["desc_index"]].text()

                r_type = 0 if r_balance - total_balance >= 0 else 1

                result.append({
                    "date": r_date,
                    "amount": r_amount,
                    "desc": r_desc,
                    "type": r_type
                })
                total_balance = r_balance

            except ValueError as e:
                print(f"Unable to proceed on the row #{e}")
    return result


if __name__ == "__main__":
    pdf_path = "eStatement.pdf"  # Replace with the path to your PDF file
    for r in get_trans_records(pdf_path):
        if r["type"] == 0:
            print(r)
