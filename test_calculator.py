import allure
from calculator import add


@allure.feature('Calculator')
@allure.story('Addition')
@allure.title('Test addition with positive numbers')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag('smoke', 'high')
def test_add_positive_numbers():
    with allure.step('Test adding 1 and 2'):
        result = add(1, 2)
        allure.attach(str(result), name='Result of 1 + 2', attachment_type=allure.attachment_type.TEXT)
        assert result == 3
    
    with allure.step('Test adding 10 and 20'):
        result = add(10, 20)
        allure.attach(str(result), name='Result of 10 + 20', attachment_type=allure.attachment_type.TEXT)
        assert result == 30


@allure.feature('Calculator')
@allure.story('Addition')
@allure.title('Test addition with zero')
@allure.severity(allure.severity_level.NORMAL)
@allure.tag('regression', 'medium')
def test_add_with_zero():
    with allure.step('Test adding 0 and 0'):
        result = add(0, 0)
        allure.attach(str(result), name='Result of 0 + 0', attachment_type=allure.attachment_type.TEXT)
        assert result == 0
    
    with allure.step('Test adding 5 and 0'):
        result = add(5, 0)
        allure.attach(str(result), name='Result of 5 + 0', attachment_type=allure.attachment_type.TEXT)
        assert result == 5


@allure.feature('Calculator')
@allure.story('Addition')
@allure.title('Test addition with negative numbers')
@allure.severity(allure.severity_level.NORMAL)
@allure.tag('regression', 'medium')
def test_add_negative_numbers():
    with allure.step('Test adding -1 and 1'):
        result = add(-1, 1)
        allure.attach(str(result), name='Result of -1 + 1', attachment_type=allure.attachment_type.TEXT)
        assert result == 0
    
    with allure.step('Test adding -5 and -3'):
        result = add(-5, -3)
        allure.attach(str(result), name='Result of -5 + -3', attachment_type=allure.attachment_type.TEXT)
        assert result == -8


@allure.feature('Calculator')
@allure.story('Addition')
@allure.title('Test addition with floating point numbers')
@allure.severity(allure.severity_level.MINOR)
@allure.tag('regression', 'low')
def test_add_float_numbers():
    with allure.step('Test adding 1.5 and 2.5'):
        result = add(1.5, 2.5)
        allure.attach(str(result), name='Result of 1.5 + 2.5', attachment_type=allure.attachment_type.TEXT)
        assert result == 4.0
    
    with allure.step('Test adding 0.1 and 0.2'):
        result = add(0.1, 0.2)
        allure.attach(str(result), name='Result of 0.1 + 0.2', attachment_type=allure.attachment_type.TEXT)
        assert abs(result - 0.3) < 1e-10


@allure.feature('Calculator')
@allure.story('Edge Cases')
@allure.title('Test addition with large numbers')
@allure.severity(allure.severity_level.MINOR)
@allure.tag('regression', 'low')
def test_add_large_numbers():
    with allure.step('Test adding large positive numbers'):
        result = add(1000000, 2000000)
        allure.attach(str(result), name='Result of 1000000 + 2000000', attachment_type=allure.attachment_type.TEXT)
        assert result == 3000000
    
    with allure.step('Test adding large negative numbers'):
        result = add(-1000000, -2000000)
        allure.attach(str(result), name='Result of -1000000 + -2000000', attachment_type=allure.attachment_type.TEXT)
        assert result == -3000000
