import boto3
import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

import boto3
from django.core.mail import send_mail

from django.core.mail.backends.smtp import EmailBackend
from django.conf import settings
class MyApi_Tag1(APIView):
    def get(self, request):

        s3 = boto3.resource('s3', aws_access_key_id='AKIA2ZMQ4SRM3OK5MNNL',
                            aws_secret_access_key='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',
                            region_name='us-east-1'
                            )

        obj = s3.Object('ec2-obd2-bucket', '866039048578802/Data/866039048578802_lat_lon_initial.txt')
        #key = obj.key
        body = obj.get()['Body'].read()
        my_json = body.decode('utf8').replace("'", '"')
        json_data = json.dumps(my_json, default=lambda o: o.__dict__, indent=4)
        # bucket = s3.Bucket('ec2-obd2-bucket')
        # for obj in bucket.objects.all():
        #    key = obj.key
        #    body = obj.get()['Body'].read()
        #    print('fileName :', key, 'filecontent:', body)

        return HttpResponse(my_json, "application/json")
class MyApi_Tag2(APIView):
    def get(self, request):

        s3 = boto3.resource('s3', aws_access_key_id='AKIA2ZMQ4SRM3OK5MNNL',
                            aws_secret_access_key='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',
                            region_name='us-east-1'
                            )

        obj = s3.Object('ec2-obd2-bucket', '866039048589288/Data/866039048589288_lat_lon_initial.txt')
        #key = obj.key
        body = obj.get()['Body'].read()
        my_json = body.decode('utf8').replace("'", '"')
        json_data = json.dumps(my_json, default=lambda o: o.__dict__, indent=4)
        # bucket = s3.Bucket('ec2-obd2-bucket')
        # for obj in bucket.objects.all():
        #    key = obj.key
        #    body = obj.get()['Body'].read()
        #    print('fileName :', key, 'filecontent:', body)

        return HttpResponse(my_json, "application/json")

class MyApi_Tag3(APIView):
    def get(self, request):

        s3 = boto3.resource('s3', aws_access_key_id='AKIA2ZMQ4SRM3OK5MNNL',
                            aws_secret_access_key='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',
                            region_name='us-east-1'
                            )

        obj = s3.Object('ec2-obd2-bucket', '866039048589957/Data/866039048589957_lat_lon_initial.txt')
        #key = obj.key
        body = obj.get()['Body'].read()
        my_json = body.decode('utf8').replace("'", '"')
        json_data = json.dumps(my_json, default=lambda o: o.__dict__, indent=4)
        # bucket = s3.Bucket('ec2-obd2-bucket')
        # for obj in bucket.objects.all():
        #    key = obj.key
        #    body = obj.get()['Body'].read()
        #    print('fileName :', key, 'filecontent:', body)

        return HttpResponse(my_json, "application/json")


class MyApi_Rpm_Tag1(APIView):
    def get(self, request):
        s3 = boto3.resource('s3', aws_access_key_id='AKIA2ZMQ4SRM3OK5MNNL',
                            aws_secret_access_key='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',
                            region_name='us-east-1'
                            )

        obj = s3.Object('ec2-obd2-bucket', '866039048578802/Data/866039048578802_rpm.txt')
        # key = obj.key
        body = obj.get()['Body'].read()
        my_json = body.decode('utf8').replace("'", '"')
        json_data = json.dumps(my_json, default=lambda o: o.__dict__, indent=4)
        new_json = json.loads(my_json)
        RPM = new_json["RPM"]
        # bucket = s3.Bucket('ec2-obd2-bucket')
        # for obj in bucket.objects.all():
        #    key = obj.key
        #    body = obj.get()['Body'].read()
        #    print('fileName :', key, 'filecontent:', body)
        return HttpResponse(my_json, "application/json")

class MyApi_Rpm_Tag2(APIView):
    def get(self, request):
        s3 = boto3.resource('s3', aws_access_key_id='AKIA2ZMQ4SRM3OK5MNNL',
                            aws_secret_access_key='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',
                            region_name='us-east-1'
                            )

        obj = s3.Object('ec2-obd2-bucket', '866039048578957/Data/866039048578957_rpm.txt')
        # key = obj.key
        body = obj.get()['Body'].read()
        my_json = body.decode('utf8').replace("'", '"')
        json_data = json.dumps(my_json, default=lambda o: o.__dict__, indent=4)
        new_json = json.loads(my_json)
        RPM = new_json["RPM"]
        # bucket = s3.Bucket('ec2-obd2-bucket')
        # for obj in bucket.objects.all():
        #    key = obj.key
        #    body = obj.get()['Body'].read()
        #    print('fileName :', key, 'filecontent:', body)
        return HttpResponse(my_json, "application/json")
