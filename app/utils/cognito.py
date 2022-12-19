import os
from typing import Any
from typing import List

import boto3


def list_users_in_admin() -> List[Any]:

    COPILOT_ENVIRONMENT_NAME = os.environ.get("COPILOT_ENVIRONMENT_NAME", "localhost")

    if COPILOT_ENVIRONMENT_NAME == "localhost":
        # ローカル環境
        client = boto3.client(
            "cognito-idp",
            region_name=os.environ.get("AWS_REGION", "ap-northeast-1"),
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        )
    else:
        # AWS環境ではECS Task Roleの権限で実行
        client = boto3.client(
            "cognito-idp",
            region_name=os.environ.get("AWS_REGION", "ap-northeast-1"),
        )

    response = client.list_users_in_group(
        UserPoolId=os.environ["COGNITO_USER_POOL_ID"],
        GroupName="admin",
    )
    # emails = []
    # for User in response["Users"]:
    #     for Attribute in User["Attributes"]:
    #         if Attribute["Name"] == "email":
    #             emails.append(Attribute["Value"])
    #         if Attribute["Name"] == "sub":
    #             emails.append(Attribute["Value"])
    # return emails
    return response
