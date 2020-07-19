import pandas as pd
from sklearn import datasets
import numpy as np

group = ['A', 'B', 'C', 'D', 'E']
table1_data = pd.DataFrame({"id": np.random.randint(995, 1005, 20),
                            "age": np.random.randint(24, 45, 20),
                            "group": [group[x] for x in np.random.randint(0, len(group), 20)],
                            "order_id": np.random.randint(1, 10, 20)})

table2_data = pd.DataFrame({"id": np.random.randint(995, 1005, 20),
                            "sales": np.random.randint(100000, 150000, 20)})

# 1. SELECT * FROM data
print(table1_data)

# 2. SELECT * FROM data LIMIT 10
print(table1_data[0:10])

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print(table1_data['id'])

# 4. SELECT COUNT(id) FROM data;
print(table1_data['id'].count())

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(table1_data[(table1_data['id'] < 1000) & (table1_data['age'] > 30)])

# 6. SELECT id, COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(table1_data.groupby('id').aggregate({"order_id": "count"}))

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(pd.merge(table1_data, table2_data, on='id'))

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([table1_data, table2_data]))

# 9. DELETE FROM table1 WHERE id=10;
print(table1_data.drop(table1_data[table1_data['id']<1000].index))

# 10. ALTER TABLE table1 DROP COLUMN column_name;
print(table1_data.drop('order_id', axis=1))