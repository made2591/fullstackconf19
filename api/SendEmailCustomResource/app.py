from crhelper import CfnResource
import boto3

ses = boto3.client('ses')
helper = CfnResource()


@helper.create
@helper.update
def notify(event, _):
    email_from = event['ResourceProperties']['EmailFrom']
    email_to = event['ResourceProperties']['EmailTo']
    email_subject = event['ResourceProperties']['InitEmailSubject']
    email_body = event['ResourceProperties']['InitEmailBody']
    helper.Data['MessageId'] = ses.send_email(
        Source=email_from,
        Destination={
            'ToAddresses': [email_to]
        },
        Message={
            'Subject': {'Data': email_subject},
            'Body': {
                'Text': {'Data': email_body}
            }
        }
    )['MessageId']


@helper.delete
def notify(event, __):
    email_from = event['ResourceProperties']['EmailFrom']
    email_to = event['ResourceProperties']['EmailTo']
    email_subject = event['ResourceProperties']['DeletionEmailSubject']
    email_body = event['ResourceProperties']['DeletionEmailBody']
    helper.Data['MessageId'] = ses.send_email(
        Source=email_from,
        Destination={
            'ToAddresses': [email_to]
        },
        Message={
            'Subject': {'Data': email_subject},
            'Body': {
                'Text': {'Data': email_body}
            }
        }
    )['MessageId']


def handler(event, context):
    helper(event, context)
