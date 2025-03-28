import boto3

s3 = boto3.resource('s3')
bucket_name = 's3-crud-akh'

all_buckets = [bucket.name for bucket in s3.buckets.all()]
# print(all_buckets)
print(bucket_name in all_buckets)

if bucket_name in all_buckets:
    print(f'{bucket_name} already exists in s3.')
else:
    s3.create_bucket(Bucket = bucket_name)
    print(f'{bucket_name} bucket create in s3.')

all_buckets = [bucket.name for bucket in s3.buckets.all()]
# print(all_buckets)
print(bucket_name in all_buckets)

if bucket_name in all_buckets:
    print(f'{bucket_name} already exists in s3.')
else:
    s3.create_bucket(Bucket = bucket_name)
    print(f'{bucket_name} bucket create in s3.')

file1 = 'file1.txt'
file2 = 'file2.txt'

s3.Bucket(bucket_name).upload_file(Filename = file1, Key = file1)

obj = s3.Object(bucket_name, file1)
body = obj.get()['Body'].read()
print(body)

obj.put(Body = open(file2, 'rb'))
body = obj.get()['Body'].read()
print(body)

obj.delete()

s3.Bucket(bucket_name).delete()