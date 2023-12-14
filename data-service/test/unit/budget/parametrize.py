header = "balance,year"
data_row = "1000.50,2013"

csv_rows = [header, data_row]


invalid_headers = "invalid,transaction_year"
invalid_data_rows = [
    "500.25,2022",
    "1200.75,2019",
    "800.00,2020",
    "1500.50,2021",
    "300.80,2018"
]

invalid_csv_rows = [invalid_headers] + invalid_data_rows


invalid_len_header = "balance,year,year"
invalid_len_csv_rows = [invalid_len_header] + invalid_data_rows
