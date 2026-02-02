Problem: Slow processing of large POS data (70GB/day)

Client issue:
The client was struggling to process large daily point-of-sale data, which caused delays in reports and decision-making.

My solution:
I built scalable Spark pipelines using Apache Spark on distributed clusters and applied caching and broadcast joins to optimize performance.

Impact:
Data processing time was significantly reduced, and daily reports were available on time.

2. Problem: No proper data model for sales analysis

Client issue:
Raw POS data had no structure, making it difficult to analyze sales by store, product, or salesperson.

My solution:
I designed fact and dimension tables (store, product, customer, time) using SQL and Spark to create a structured data model.

Impact:
Business teams could easily analyze sales trends and performance at different levels.

3. Problem: Low sales team motivation due to lack of performance tracking

Client issue:
Sales staff were not motivated because performance was not tracked or rewarded clearly.

My solution:
I helped design an incentive program by calculating top performers using sales data and ranking logic in Spark and SQL.

Impact:
Salesperson motivation increased, leading to better sales performance across stores.

4. Problem: Manual and unreliable data pipelines

Client issue:
Data pipelines were manually triggered, which caused failures and inconsistency in data availability.

My solution:
I automated workflows using Airflow DAGs and CRON jobs, and integrated deployments using Azure CI/CD pipelines.

Impact:
Pipelines became reliable, repeatable, and required minimal manual intervention.

5. Problem: Customer churn due to infrequent buyers

Client issue:
The client was losing customers who stopped purchasing frequently.

My solution:
I built logic to identify infrequent buyers using historical purchase data and enabled a coupon-based incentive system.

Impact:
Customer retention improved, and repeat purchases increased, boosting overall revenue.


Welcome to the show. This endeavor aims to provide you with insights into the functioning of projects within a real-time environment.

The code has been meticulously crafted with careful consideration for various aspects. It not only nurtures your coding skills but also imparts a comprehensive comprehension of project structures.

Let's Start with requirement to complete the projects:-
1. You should have laptop with minimum 4 GB of RAM, i3 and above (Better to have 8GB with i5).
2. Local setup of spark. This is tricky so keep all things intact to work it properly.Download python 3.10.11 instead of python3.6 or python3.9 
3. PyCharm installed in the system. How to install
4. MySQL workbench should also be installed to the system. How to install
5. GitHub account is good to have but not necessary.
5. You should have AWS account. How to create:- 
6. Understanding of spark,sql and python is required.

```plaintext
Project structure:-
my_project/
├── docs/
│   └── readme.md
├── resources/
│   ├── __init__.py
│   ├── dev/
│   │    ├── config.py
│   │    └── requirement.txt
│   └── qa/
│   │    ├── config.py
│   │    └── requirement.txt
│   └── prod/
│   │    ├── config.py
│   │    └── requirement.txt
│   ├── sql_scripts/
│   │    └── table_scripts.sql
├── src/
│   ├── main/
│   │    ├── __init__.py
│   │    └── delete/
│   │    │      ├── aws_delete.py
│   │    │      ├── database_delete.py
│   │    │      └── local_file_delete.py
│   │    └── download/
│   │    │      └── aws_file_download.py
│   │    └── move/
│   │    │      └── move_files.py
│   │    └── read/
│   │    │      ├── aws_read.py
│   │    │      └── database_read.py
│   │    └── transformations/
│   │    │      └── jobs/
│   │    │      │     ├── customer_mart_sql_transform_write.py
│   │    │      │     ├── dimension_tables_join.py
│   │    │      │     ├── main.py
│   │    │      │     └──sales_mart_sql_transform_write.py
│   │    └── upload/
│   │    │      └── upload_to_s3.py
│   │    └── utility/
│   │    │      ├── encrypt_decrypt.py
│   │    │      ├── logging_config.py
│   │    │      ├── s3_client_object.py
│   │    │      ├── spark_session.py
│   │    │      └── my_sql_session.py
│   │    └── write/
│   │    │      ├── database_write.py
│   │    │      └── parquet_write.py
│   ├── test/
│   │    ├── scratch_pad.py.py
│   │    └── generate_csv_data.py
```

How to run the program in Pycharm:-
1. Open the pycharm editor.
2. Upload or pull the project from GitHub.
3. Open terminal from bottom pane.
4. Goto virtual environment and activate it. Let's say you have venv as virtual environament.i) cd venv ii) cd Scripts iii) activate (if activate doesn't work then use ./activate)
5. Create main.py as explained in my videos on YouTube channel.
6. You will have to create a user on AWS also and assign s3 full access and provide secret key and access key to the config file.
6. Run main.py from green play button on top right hand side.
7. If everything works as expected enjoy, else re-try.

Project Architecture:-
![Architecture](C:\Users\nikita\Pictures\Screenshots\architecture.png)

Database ER Diagram:-
![Architecture](C:\Users\nikita\Documents\data_engineering\pythonProject\youtube_project\docs\database_schema.drawio.png)

If you get stuck, don't forget to my watch my youtube channel project playlist for better understanding of the flow.
