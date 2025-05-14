from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.transforms import *

# Create GlueContext
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Read data from S3
input_dynamic_frame = glueContext.create_dynamic_frame.from_catalog(database = "your_database_name", table_name = "your_table_name")

# Convert to DataFrame for easier manipulation
input_data_frame = input_dynamic_frame.toDF()

# Perform transformation (Example: Selecting specific columns)
transformed_data_frame = input_data_frame.select("col1", "col2")

# Convert DataFrame back to DynamicFrame
transformed_dynamic_frame = DynamicFrame.fromDF(transformed_data_frame, glueContext, "transformed_dynamic_frame")

# Write the transformed data back to S3
output_path = "s3://your-output-bucket/output-data/"
glueContext.write_dynamic_frame.from_options(
    frame = transformed_dynamic_frame,
    connection_type = "s3",
    connection_options = {"path": output_path},
    format = "csv"
)

# Stop the Spark context
sc.stop()
