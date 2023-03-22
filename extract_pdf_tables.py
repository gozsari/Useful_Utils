import tabula
import pandas as pd
pdf_file = "files/dataset_add_info.pdf"
page_no = 6
table_no = 2
dfs = tabula.read_pdf(pdf_file, pages=page_no)

dfs[table_no].to_csv(f"tables_csv/table_{table_no}.csv", index=False)
dfs[table_no].to_excel(f"tables_csv/table_{table_no}.xlsx", index=False)