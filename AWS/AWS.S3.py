# Reding the last line[Footer] [Trailer] and first line[Header]
import boto3

# Initialize the S3 client
s3 = boto3.client('s3')


# Specify the bucket name and file key
bucket_name = 'your_bucket_name'
file_key = 'path/to/your/file.txt'

# Get the object from S3
header_response = s3.get_object(Bucket=bucket_name, Key=file_key)

# Read all lines and select the last one
last_line_bytes = header_response['Body'].readlines()[-1]

# Read header
header = header_response['Body'].readline()

# Decode the bytes and strip leading/trailing whitespace
last_line = last_line_bytes.decode().strip()[5:]
header_line = header.decode().strip()



print("Last line of the file:", last_line)
