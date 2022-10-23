import boto3


client = boto3.client('dynamodb', aws_access_key_id="AKIA6JN56SFDTB66CQKO",
                      aws_secret_access_key="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",
                      region_name="ap-northeast-1")

def get_item(pk, sk):
    res = client.get_item(
        TableName="Students",
        Key={
            "student": {"S": pk},
            "class": {"S": sk}
        },
        ProjectionExpression="#c",
        ExpressionAttributeNames={"#c":"class"}
    )

    return res

print(get_item("Le Duc Thang", "AWS"))
