import json
import allure
from allure_commons.types import AttachmentType
from requests import Response


def request_attaching(response: Response):

    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    allure.attach(body=response.request.method, name="Method", attachment_type=AttachmentType.TEXT)
    allure.attach(body=json.dumps(dict(response.request.headers), indent=4), name="Request headers", attachment_type=AttachmentType.JSON)

    if response.request.body:
        allure.attach(
            body=json.dumps(response.request.body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )


def response_attaching(response: Response):

    allure.attach(body=str(response.status_code), name="Code", attachment_type=AttachmentType.TEXT)
    allure.attach(body=json.dumps(dict(response.request.headers), indent=4), name="Response headers", attachment_type=AttachmentType.JSON)
    allure.attach(body=json.dumps(dict(response.cookies), indent=4), name="Cookies", attachment_type=AttachmentType.JSON)


    if response.text:
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
