# Import Libraries
import boto3
import io
import zipfile
import mimetypes

def lambda_handler(event, context):
    # SNS Resource and Topic
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:813570147528:deployS3PortfolioTopic')
    
    try: 
        # S3 Resource
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
        topic.publish(Subject="Portfolio Deployment Success", Message="Latest portfolio succesfully deployed to S3.")
    except:
        topic.publish(Subject="Portfolio Deployment Failed", Message="Portfolio was not deployed succesfully.")
        raise

    return "Lambda function deployS3Website succesfully ran."
		
