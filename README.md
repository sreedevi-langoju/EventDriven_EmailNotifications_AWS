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
* Notedown the SNS Topic ARN value.

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
* Click "Create function".

#### Step 5: Write Lambda Function Code
* Write the Lambda function code to count words in the uploaded text file. 
 (OR)
* Delete the existing code in the  Lambda Code area and copy the paste the python code from wordcount.py file in this repository.
* In the Function overview section, scroll down to the "Function code" panel.
* In the "Environment variables" section, click the "Edit" button to add environmental variables.
* Add a new environmental variable with a key like SNS_TOPIC_ARN and the value set to your SNS topic's ARN.
* Add SNS Topic ARN Variable
* Click "Save" to save the environmental variable.

#### Step 6: Configure S3 Event Trigger for Lambda

* Go to your Lambda function in the AWS Lambda console.
* Click "Add trigger" and select "S3."
* Configure the trigger with the S3 bucket you created in Step 1 and set event type to "ObjectCreated (All)."
* Click "Add."

#### Step 7: Configure SNS Notification

* Go to your Lambda function in the AWS Lambda console.
* Click on the "Designer" tab.
* Click on the Lambda function box and then click on "Add destination."
* Choose "SNS" as the destination and select the SNS topic you created in Step 2.
* Click "Save" to configure the notification.

#### Step 8: Upload a Text File to S3
Upload a text file to the S3 bucket. This will trigger the Lambda function, which will count the words and send a notification to the SNS topic.

#### Step 9: Receive Word Count Report
The SNS topic will send a notification to the specified email address with the word count report whenever a text file is uploaded to the S3 bucket.

You have now set up a Lambda function to count words in a text file, configured S3 to trigger the Lambda function, and created an SNS topic to report the word count via email notifications.


