import boto3
print('Boto3 imported')

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)