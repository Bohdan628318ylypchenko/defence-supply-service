HEADERS = "supply_name,unit_count,expiration_date"
DATA_ROWS = [
    "Supply1,100,2023-12-31",
    "Supply2,50,2023-11-15",
    "Supply3,75,2023-10-01",
    "Supply4,120,2023-09-05",
    "Supply5,80,2023-08-20"
]

CSV_ROWS = [HEADERS] + DATA_ROWS

INVALID_HEADERS = "supply,unit_count,expiration_date"
INVALID_HEADERS_LEN = "supply_name,supply_name,unit_count,expiration_date"

INVALID_HEADERS_CSV_ROWS = [INVALID_HEADERS] + CSV_ROWS
INVALID_HEADERS_LEN_CSV_ROWS = [INVALID_HEADERS_LEN] + CSV_ROWS
