import boto3

# Initialize a session using Amazon S3 credentials
session = boto3.Session(
    aws_access_key_id='ASIAVMUUZ2FJZUCQUPEL',
    aws_secret_access_key='42qMeQJ029lasY+6TAePtQetLj2w22dlSFlDu+7K',
    region_name='us-east-1'
)


# Initialize S3 client
# s3 = session.client('s3')
s3 = boto3.resource('s3')

# # Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# def copy_s3_objects(source_bucket, target_bucket):
#     # List objects within the source bucket
    # objs = s3.list_objects_v2d(Bucket=source_bucket)['Contents']
    
    # for obj in objs:
    #     copy_source = {
    #         'Bucket': source_bucket,
    #         'Key': obj['Key'],
    #         'VersionId': obj['VersionId']  # Preserving the version ID
    #     }
        
    #     # Copy object to the target bucket
    #     s3.copy_object(
    #         CopySource=copy_source,
    #         Bucket=target_bucket,
    #         Key=obj['Key']
    #     )
    #     print(f"Copied {obj['Key']} from {source_bucket} to {target_bucket} with VersionId {obj['VersionId']}")

# # Replace 'source-bucket-name' and 'target-bucket-name' with your bucket names
# copy_s3_objects('helana-test', 'helana-test2')

