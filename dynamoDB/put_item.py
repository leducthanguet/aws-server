from http import client
import boto3

client = boto3.client('dynamodb', aws_access_key_id="AKIA6JN56SFDTB66CQKO",
                      aws_secret_access_key="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",
                      region_name="ap-northeast-1")

res = client.put_item(
    TableName='Students',
    Item={
        "student": {"S": "Le Duc Tinh"},
        "class": {"S": "ILETS"},
        "level": {"S": "MIDDLE"},
        "score": {"N": "10.0"},
        "special_attr": {"L": [
            {"L": [{"S": "A"}, {"S": "B"}]}, 
            {"L": [{"S": "C"}, {"S": "D"}]}
        ]}
    },
    ConditionExpression='attribute_exists(student)'
)
print(res)
