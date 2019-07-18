import boto3
import io
import zipfile
import mimetypes

s3 = boto3.resource('s3')

portfolio_bucket = s3.Bucket('portfolio.nolimitsnick.com')
build_bucket = s3.Bucket('portfoliobuild.nolimitsnick.com')

portfolio_zip = io.BytesIO()
build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
	for item in myzip.namelist():
		obj = myzip.open(item)
		portfolio_bucket.upload_fileobj(obj, item, ExtraArgs={'ContentType': mimetypes.guess_type(item)[0]})
		portfolio_bucket.Object(item).Acl().put(ACL='public-read')
		


