from models.pushpull.Pushpulltosql import pull
from models.db.Utils_database import get_connection
from models.db.database_with_classes import create_tables, delete_all_tables


conn, mycursor = get_connection('./data/electronic_store_with_classes.db')
cap_num, cap_list = pull('capacitor')
ic_num, ic_list = pull('ic')
res_num, res_list = pull('resistor')
ind_num, ind_list = pull('inductor')
sen_num, sen_list = pull('sensor')
manu_num, manu_list = pull('manufacturer')


print(cap_list)
