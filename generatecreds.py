# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 06:20:31 2020

@author: rnach
"""

import os
import boto3
from dotenv import load_dotenv

load_dotenv()


AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

client = boto3.client( 'iam', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY )

response = client.generate_credential_report()