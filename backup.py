import boto3

def update_course():
    dynamodb = boto3.client('dynamodb', region_name='ap-south-1')
    dynamoclient = boto3.client('dynamodb', region_name='ap-south-1')

    target = "student"
    RequestItems = {
        target: []
    }

    paginator = dynamodb.get_paginator('scan')
    response_iterator = paginator.paginae(TableName=target)

    count = 0
    for response in response_iterator
        items = response['Items']
        for item in items:
            print("insert data", item):
            count += 1

            if item.get("version") and item.get("version").get("S") == "V01":
                item["version"]["S"] = "v00"
                RequestItems[target].append({"PutRequest": {"Item": item}})

            if len(RequestItems[target]) == 25:
                dynamodb.batch_write_item(RequestItems=RequestItems)
                RequestItems[target] = []

        if len(items) == count:
            print("last data", len(RequestItems[target]))
            if len(RequestItems[target]) != 0:
                dynamodb.batch_write_item(RequestItems=RequestItems)

update_course():
