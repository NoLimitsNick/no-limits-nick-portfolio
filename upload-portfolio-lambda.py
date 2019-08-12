# Import Libraries
import boto3
import io
import zipfile
import mimetypes

def lambda_handler(event, context):
    # S3 from boto3 AWS SDK
    s3 = boto3.resource('s3')
    
    # Get Target Bucket and BuildBucket
    target_buccket = s3.Bucket('portfolio.nolimitsnick.com')
    build_bucket = s3.Bucket('portfoliobuild.nolimitsnick.com')
    
    # Buffer Stream to String and Download 
    target_zip = io.BytesIO()
    build_bucket.download_fileobj('portfoliobuild.zip', target_zip)
    
    # Unzip file, upload, and update ACL with Public Read
    with zipfile.ZipFile(target_zip) as myzip:
    	for item in myzip.namelist():
    		obj = myzip.open(item)
    		target_buccket.upload_fileobj(obj, item, ExtraArgs={'ContentType': mimetypes.guess_type(item)[0]})
    		target_buccket.Object(item).Acl().put(ACL='public-read')
    
    print('Succesfully Pushed Latest Portfolio Build to S3')
    
    return "Lambda function deployS3Website succesfully ran"
		


