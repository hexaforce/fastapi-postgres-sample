import random
import string
import requests


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"

def csrftoken() -> str:
    r = requests.get("http://api/api/v2/csrftoken")
    return r.json()["csrf_token"]

def headers_token() -> str:
    ADMIN_TOKEN = "eyJraWQiOiJwZTZIWjhTSXpweERiM1MwMUJET2F5ZTB1ZmtxamNYUGJhaDMrNVpBVmd3PSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxZWE2YzgyZi0xZDg3LTQ0MmYtYmIyNS1mYmRmZjhmNzc2ZWMiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb21cL2FwLW5vcnRoZWFzdC0xX0pFcnc0c0NzWiIsImNvZ25pdG86dXNlcm5hbWUiOiIxZWE2YzgyZi0xZDg3LTQ0MmYtYmIyNS1mYmRmZjhmNzc2ZWMiLCJvcmlnaW5fanRpIjoiYzE4ODJiODctOTNhMC00YTQyLTg2MGUtZWY4NDg0Yzk1OWE2IiwiYXVkIjoiMzliNWo2NnR2OGxmcHNkNXE3Y3Y2cTU3dG8iLCJldmVudF9pZCI6IjU0YTcwNzk4LWQ0NTItNDdkYS1iM2JiLTAzZGMyN2RkMmRlYyIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjUwNjA2MTMxLCJleHAiOjE2NTA2MDk3MzEsImlhdCI6MTY1MDYwNjEzMSwianRpIjoiZTA1OGYwYTItMDliMi00OTQ2LTllZGYtMGExZmExOWEzZDIwIiwiZW1haWwiOiJhcGlAdmlldy1zdGcuYWlyZGVzaWduLmFpIn0.HkFqOClvc5250fwoBt57LJ6lDzkG8Rq7Vm1HRuiRF9t_ddP4D_3dW5zCn5M24KChTi7dYMGIvTDErUEmYbKgoRmxUdKzF6PR-PRIvXRLmxP9P5ZBdvHZ2YXvml5X7bsR5X2EQxdDXqjqlpavhZDxc-6YEyRzypITuF9Y-1ZQZJ0t6N1DLf-9KrCSbapbBFXwaF82ZBli57vM-K6fcHNV3fCajNfoyzAfKJQvkF4QHWOC_WH6UqwsMgo6Hnr27zg1DHX1SJMXb1S0rRod8TM8NPChLTvHXw894RMai4CRoc1yAEDmm3MwKwSx3t_eq4-CmCd2EYivrH5UGnMc5NXtsQ"
    # return {"authorization": ADMIN_TOKEN, "x-e2e": "True", "x-csrf-token": csrftoken()}
    return {"authorization": ADMIN_TOKEN}
