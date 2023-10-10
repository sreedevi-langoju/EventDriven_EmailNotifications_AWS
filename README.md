# EventDriven_EmailNotification_AWS
Event Driven Notification System using Amazon S3, Lambda, SNS 

In this project, I built an event-driven architecture by harnessing the capabilities of AWS services. The process was initiated with S3 triggers, which were captured through a Lambda function. The captured data was then seamlessly passed to Amazon SNS, enabling the automated sending of customized email notifications to customers. This setup ensured timely and efficient communication with end-users and streamlined the event-based email notification process.

<img src="https://github.com/sreedevi-langoju/EventDriven_EmailNotifications_AWS/assets/135724041/f548b8ea-da08-4320-957d-a13ffd31f44a" width="300">

#### Step 1: Create an S3 Bucket

* Go to the AWS S3 console.
* Click "Create bucket" and follow the wizard to create a new bucket or select an existing one.

#### Step 2: Create an SNS Topic

* Go to the AWS SNS console.
* Click "Create Topic" and follow the wizard to create a new SNS topic.
* Configure the topic with a name and display name. You will use this topic to send word count notifications.
* Need to subscribe to this SNS topic.

#### Step 3: Create an IAM Role for Lambda

* Go to the AWS IAM console.
* Create a new IAM role with permissions to execute Lambda functions, read from the S3 bucket, and publish to the SNS topic.
* Attach the following policies to the role:
* AWSLambdaBasicExecutionRole (for Lambda execution)
* AmazonS3ReadOnlyAccess (for reading from S3)
* AmazonSNSFullAccess (for publishing to SNS)

#### Step 4: Create the Lambda Function

* Go to the AWS Lambda console.
* Click "Create function" and select "Author from scratch."
* Configure your function:
* Name: Choose a name for your Lambda function.
* Runtime: Select the appropriate runtime for your code (e.g., Python, Node.js, etc.).Here I am choosing Python 3.11
* Execution role: Choose "Use an existing role" and select the IAM role created in Step 3.
* Click "Create function."
