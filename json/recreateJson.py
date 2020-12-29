import sqlite3
import json

conn = sqlite3.connect('51job_py_java_c++.db')
c = conn.cursor()
# print "Opened database successfully"

job_category_list = ['python', 'java', 'c++']
company_type_list = ["上市公司","民营公司","创业公司","事业单位","外资（欧美）","外资（非欧美）","国企","合资","政府机关","非营利组织","外企代表处"]
json_data = []
# cursor = c.execute("SELECT * FROM job");
for company in company_type_list:
    pro_item = {'company_type': company}
    for job in job_category_list:
        cursor = c.execute(
            "SELECT count(company_type), job_category from job where job_category = ? and company_type = ?;",
            (job, company))
        for row in cursor:
            if 'python' in job:
                pro_item["py_requirement"] = row[0]
            if 'java' in job:
                pro_item["java_requirement"] = row[0]
            if 'c++' in job:
                pro_item["cpp_requirement"] = row[0]
    print(pro_item)
    json_data.append(pro_item)

with open('company_job.json', 'w') as f:
    json.dump(json_data, f)



