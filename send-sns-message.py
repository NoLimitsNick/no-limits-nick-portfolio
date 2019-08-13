import boto3

sns = boto3.resource('sns')
topic = sns.Topic('arn:aws:sns:us-east-1:813570147528:deployS3PortfolioTopic')
response = topic.publish(Subject="Test Message # 3", Message="Python Script with response")

print(response)
