import allure
import pytest
import os
import json
from datetime import datetime


def pytest_configure(config):
    if not os.path.exists('allure-results'):
        os.makedirs('allure-results')
    
    environment_properties = {
        'Browser': 'Chrome',
        'Browser.Version': 'latest',
        'OS': 'Windows',
        'Python.Version': '3.x',
        'Test.Environment': 'Local'
    }
    
    with open('allure-results/environment.properties', 'w') as f:
        for key, value in environment_properties.items():
            f.write(f'{key}={value}\n')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == 'call' and report.failed:
        try:
            allure.attach(
                f'Test failed at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
                name='Failure Time',
                attachment_type=allure.attachment_type.TEXT
            )
        except Exception:
            pass


@pytest.fixture(scope='session', autouse=True)
def session_setup():
    with allure.step('Session Setup - Initialize test environment'):
        yield
    with allure.step('Session Teardown - Clean up test environment'):
        pass


@pytest.fixture(scope='function', autouse=True)
def test_setup(request):
    test_name = request.node.name
    with allure.step(f'Test Setup - Prepare for {test_name}'):
        yield
    with allure.step(f'Test Teardown - Clean up after {test_name}'):
        pass
