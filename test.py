from models.db.pull_from_db import get_rows
from models.db.push_to_db import create_row, update_row
from models.db.utils.create_query import like, start_from, contains
from models.db.functions import get_all_tables, delete_all_tables

# print(where_conditions(["a = 4"]))

# result = pull_from_db("ic")
# print(len(result))
# for r in result:
#     print(r)

# push_to_db("ic", ["part124", "M002", 10, "2023-09-02", 22, 22, "Something", 222, "IC9.png"])

# update_row("ic", {"sub_category": "now"}, ("part_number", "part124"))
# result = get_rows("ic")
# print(len(result))
# for r in result:
#     print(r)

print(get_all_tables())
delete_all_tables()
print(get_all_tables())