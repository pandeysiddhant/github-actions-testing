import pytest
from pytest_bdd import scenarios, given, when, then, parsers

# Load the feature file
scenarios("test.feature")

@pytest.fixture
def context():
    return {}

@given(parsers.parse("Two integers are given {x:d} and {y:d}"))
def given_two_integers(context, x, y):
    context['x'] = x
    context['y'] = y

@when("The two of them are added")
def when_add_numbers(context):
    context['z'] = context['x'] + context['y']

@then("The sum is equal to 30")
def then_check_sum(context):
    assert context["z"] == 30

# ---------------------------------------------------------------------------

@given(parsers.parse("Their is a String provided: {String}"))
def func_first(context, String):
    context["word"] = String

@when("The reverse of the String is done")
def reverse_func(context):
    context["reverse"] = context["word"][::-1]

@then("It is a pallindrome or else not")
def check_palindrome(context):
    word = context["word"]
    reverse = context["reverse"]
    print(f"Word: {word}, Reverse: {reverse}")

    # Fail if it's not pallindrome
    if word != reverse:
        pytest.xfail(reason=f"{word} is not a palindrome")
    assert word == reverse