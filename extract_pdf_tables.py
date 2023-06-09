"""
This script extracts output from a pdf file and saves them as csv and xlsx input.
"""
import tabula
import argparse

def main():
    """Main function"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf_file', type=str, default='input/test.pdf', help='pdf file name')
    parser.add_argument('--page_no', type=int, default=6, help='page number')
    parser.add_argument('--table_no', type=int, default=2, help='table number')
    args = parser.parse_args()
    pdf_file = args.pdf_file
    page_no = args.page_no
    table_no = args.table_no
    dfs = tabula.read_pdf(f"input/{pdf_file}", pages=page_no)
    dfs[table_no].to_csv(f"output/table_{table_no}.csv", index=False)
    dfs[table_no].to_excel(f"output/table_{table_no}.xlsx", index=False)


if '__main__' == __name__:
    main()
