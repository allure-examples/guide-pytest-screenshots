import allure
import base64


from allure_commons.types import AttachmentType

def pytest_selenium_capture_debug(item, report, extra):
    for log_type in extra:
        if log_type["name"] == "Screenshot":
            content = base64.b64decode(log_type["content"].encode("utf-8"))
            allure.attach(content, name="Screenshot on failure", attachment_type=AttachmentType.PNG)
