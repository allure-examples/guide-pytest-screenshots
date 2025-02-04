import re
import allure
import pytest

from pathlib import Path

SCREENSHOT_NAME_PATTERN = re.compile(r"^test-failed-\d+\.png$")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item, nextitem):
    yield

    try:
        artifacts_dir = item.funcargs.get("output_path")
        if artifacts_dir:
            artifacts_dir_path = Path(artifacts_dir)
            if artifacts_dir_path.is_dir():
                for file in artifacts_dir_path.iterdir():
                    if file.is_file() and SCREENSHOT_NAME_PATTERN.match(file.name):
                        allure.attach.file(
                            str(file),
                            name=file.name,
                            attachment_type=allure.attachment_type.PNG,
                        )
    except Exception as e:
        print(f"Error taking screenthot: {e}")
