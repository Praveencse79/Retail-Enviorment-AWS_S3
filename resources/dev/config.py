import os

key = "youtube_project"
iv = "youtube_encyptyo"
salt = "youtube_AesEncryption"


#AWS Access And Secret key
# aws_access_key =   "CBbSUPfgl+CcJPNG5lpHuBLLaX9Zu8Lczsx3VDio8ss=" # "your_encrypted_access_key" "AKIA55MHVQWVQ7CXVXGU"
# aws_secret_key =     "51kJmEher4whvA2RTU0ab/bOz0BU8g8bs96aDVDTIjO/N9dp8vNvEIqXMXZpaheu" #"your_encrypted_secret_key" # "Ub0uoWFFUXuoTttBsfjk0JtXmdX6RVpWXZgGF2Y6"

bucket_name = "de-store-praveenyadav"
s3_customer_datamart_directory = "customer_data_mart"
s3_sales_datamart_directory = "sales_data_mart"
s3_source_directory = "sales_data/"
s3_error_directory = "sales_data_error/"
s3_processed_directory = "sales_data_processed/"


#Database credential
# MySQL database connection properties
database_name = "praveen"
url = f"jdbc:mysql://localhost:3306/{database_name}"
properties = {
    "user": "root",
    "password": "Radha@1965",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Table name
customer_table_name = "customer"
product_staging_table = "product_staging_table"
product_table = "product"
sales_team_table = "sales_team"
store_table = "store"

#Data Mart details
customer_data_mart_table = "customers_data_mart"
sales_team_data_mart_table = "sales_team_data_mart"

# Required columns
mandatory_columns = ["customer_id","store_id","product_name","sales_date","sales_person_id","price","quantity","total_cost"]


# File Download location
local_directory = "C:\\local_datastore_for_project\\date_engineering\\spark_data\\file_from_s3\\"
customer_data_mart_local_file = "C:\\local_datastore_for_project\\date_engineering\\spark_data\\customer_data_mart\\"
sales_team_data_mart_local_file = "C:\\local_datastore_for_project\\date_engineering\\spark_data\\sales_team_data_mart\\"
sales_team_data_mart_partitioned_local_file = "C:\\local_datastore_for_project\\date_engineering\\spark_data\\sales_partition_data\\"
error_folder_path_local = "C:\\local_datastore_for_project\\date_engineering\\spark_data\\error_files\\"
