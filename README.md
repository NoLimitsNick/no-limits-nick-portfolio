# No Limits Nick Portfolio
NLN The Dev
Portfolio designed using AWS and ReactJS.

AWS Services Used:
IAM		S3		CodeBuild
JS Frameworks Used:


Technologies Used:
Brew	Git/GitHub	SSH
HTML/CSS	Font Awwesome	Google Fonts
Babel		React			Chai/Mocha
Python 3.7 and Python 3.6.4 PyEnv for Multiple Versions
pyenv install 3.6.4	pyenv global 3.6.4

Documented Steps..
Step 1: SSH Setup : Machine loads private. Git loads public)
ssh -keygen -C <email_address>
ls ~/.ssh
cat id_rsa.pub
ssh-add

Created deployS3Website Lambda function to S3.
Role granted is deployS3WebsiteRole

Created SNS Notification deployS3PortfolioTopic 
aws sns publish --topic-arn arn:aws:sns:us-east-1:813570147528:deployS3PortfolioTopic --subject "Test message" --message "This is a test message"

Created Custom IAM Policy SNSPublishTo-deployPortfolioTopic 

CodePipeline Automation
Add Lambda as custom action to CodePipeline(Not natively supported as deployment)

NPM Installation
Save (Needed for Project to RUn)
npm install --save react@16.2.0 react-dom@16.2.0
save-dev (Needed for development)
npm install --save-dev webpack@4.2.0 webpack-cli@2.0.13
npm install --save-dev babel-core@6.26.0 babel-loader@7.1.4 babel-preset-react@6.24.1