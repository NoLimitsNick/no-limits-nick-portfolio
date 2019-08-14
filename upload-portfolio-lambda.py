# Import Libraries
import boto3
import io
import zipfile
import mimetypes

def lambda_handler(event, context):
    # SNS Resource and Topic
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:813570147528:deployS3PortfolioTopic')
    
    location = {
        "bucketName" : 'portfoliobuild.nolimitsnick.com',
        "objectKey" : 'portfoliobuild.zip'
    }
    
    try: 
        # CodePipeline Job
        job = event.get("CodePipeline.job")
        
        if job:
            for artifact in job["data"]["inputArtifacts"]:
                # print(artifact)
                if artifact["name"] == "BuildArtifact":
                    location = artifact["location"]["s3Location"]
                    
        print("Building portfolio from " + str(location))
        # S3 Resource
        s3 = boto3.resource('s3')
        
        # Get Target Bucket and BuildBucket
        target_bucket = s3.Bucket('portfolio.nolimitsnick.com')
        build_bucket = s3.Bucket(location["bucketName"])
        
        # Buffer Stream to String and Download 
        target_zip = io.BytesIO()
        build_bucket.download_fileobj(location["objectKey"], target_zip)
        
        # Unzip file, upload, and update ACL with Public Read
        with zipfile.ZipFile(target_zip) as myzip:
        	for item in myzip.namelist():
        		obj = myzip.open(item)
        		target_bucket.upload_fileobj(obj, item, ExtraArgs={'ContentType': mimetypes.guess_type(item)[0]})
        		target_bucket.Object(item).Acl().put(ACL='public-read')
        
        print('Succesfully Pushed Latest Portfolio Build to S3')
        topic.publish(Subject="Portfolio Deployment Success", Message="Latest portfolio succesfully deployed to S3.")
        
        if job:
            codepipeline = boto3.client("codepipeline")
            codepipeline.put_job_success_result(jobId=job["id"])
    except:
        topic.publish(Subject="Portfolio Deployment Failed", Message="Portfolio was not deployed succesfully.")
        raise

    return "Lambda function deployS3Website succesfully ran."
		
