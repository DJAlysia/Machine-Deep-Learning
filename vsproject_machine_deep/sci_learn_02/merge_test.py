# 직원 정보, 부서정보
# 공동된 컬럼으로 교집합을 구하시오

# 공동된 컬럼(emp_id, mng_id)
# 부서정보 총무 1400 으로 변경하고 교집합을 구하시오

import pandas as pd

emp_data = pd.read_csv('data/emp_data2.csv')
dept_data = pd.read_csv('data/dept_data2.csv')

dept_data.loc[dept_data['dept_name'] == '총무', 'mng_id'] = 1400

m_data = pd.merge(emp_data, dept_data, left_on='emp_id', right_on='mng_id')

print(m_data)

