HEADERS = "name,unit_cost,unit_type,norm_unit_count_day"
DATA_ROWS = [
    "Item1,10.50,Piece,100.0",
    "Item2,5.75,Box,50.5",
    "Item3,20.00,Liter,75.25",
    "Item4,15.25,Piece,120.75",
    "Item5,8.90,Box,90.0"
]

CSV_ROWS = [HEADERS] + DATA_ROWS


INVALID_HEADERS = "name,unit_cott,invalid,invalid"

INVALID_LEN_HEADERS = "name,unit_cost,unit_type,norm_unit_count_day,name"

INVALID_HEADERS_CSV_ROW = [INVALID_HEADERS] + DATA_ROWS
INVALID_LEN_HEADERS_CSV_ROW = [INVALID_LEN_HEADERS] + DATA_ROWS

