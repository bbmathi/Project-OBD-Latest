import boto3


def reads3():
    s3 = boto3.resource('s3', aws_access_key_id='AKIA2ZMQ4SRM3OK5MNNL',
                        aws_secret_access_key='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',
                        region_name='us-east-1'
                        )

    obj = s3.Object('ec2-obd2-bucket', '866039048578802/Data/866039048578802_lat_lon_initial.txt')
    key = obj.key
    body = obj.get()['Body'].read()
    print('fileName :', key, 'filecontent:', body)

    # bucket = s3.Bucket('ec2-obd2-bucket')
    # for obj in bucket.objects.all():
    #    key = obj.key
    #    body = obj.get()['Body'].read()
    #    print('fileName :', key, 'filecontent:', body)


reads3()
