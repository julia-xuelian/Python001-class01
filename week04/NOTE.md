学习笔记

1、pandas支持的数据类型为一维数组series和二维数组dataframe
2、pandas支持多种导入类型的数据：
  (1) pd.read_excel()
  (2) pd.read_csv()
  (3) pd.read_table()
  (4) sql  =  'SELECT * FROM Table'
      conn = pymysql.connect(host='hostname',user='username',passwd='password',db='database', port=port, charset='utf8')
      df = pd.read_sql(sql, conn)
3、缺失值处理：
  (1) 检查是否存在缺失值：x.hasnans
  (2) 缺失值填充
      a. 平均值填充：x.fillna(value=x.mean())
      b. 文本填充：  x.fillna('text')
      c. 前一行填充：x.ffill()
      d. 前一列填充：x.ffill(axis=1)
  (3) 缺失值删除：x.dropna()
4、数据处理：
  (1) 替换：df.replace()
  (2) 排序：df.sort_values()
  (3) 删除：
      列：df.drop('column names', axis=1)
      行：df.drop(index, axis=0)
  (4) 行列互换：
      df.T 
      df.T.T
 5、聚合：
  (1) df.groupby('column name').groups
  (2) df.groupby('column name').count()
  (3) df.groupby('column name').aggregate( {'column name':'count' , 'column name':'sum' })
  (4) df.groupby('column name').agg('mean')
  (5) df.groupby('column name').mean().to_dict()
6、数据透视表：
  pd.pivot_table(data, 
               values='salary', 
               columns='group', 
               index='age', 
               aggfunc='count', 
               margins=True  
            ).reset_index()
