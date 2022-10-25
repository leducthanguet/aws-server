import boto3


client = boto3.client('dynamodb', aws_access_key_id="",
                      aws_secret_access_key="",
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
