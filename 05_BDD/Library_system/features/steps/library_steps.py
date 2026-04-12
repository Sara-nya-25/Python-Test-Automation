from behave import given, when, then
from src.library import Library, Book

@given('the library has the following books:')
def step_impl_init(context):
    context.library = Library()
    for row in context.table:
        context.library.add_book(Book(title=row['title'], author=row['author']))

@given('"{title}" is currently on loan')
def step_impl_on_loan(context, title):
    book = context.library.find_book(title)
    book.is_on_loan = True

@when('I search for books with title "{title}"')
def step_impl_search_title(context, title):
    context.search_results = context.library.search_by_title(title)

@when('I search for books by "{author}"')
def step_impl_search_author(context, author):
    context.search_results = context.library.search_by_author(author)

@when('I borrow "{title}"')
def step_impl_borrow(context, title):
    book = context.library.find_book(title)
    if book:
        book.is_on_loan = True

@when('I return "{title}"')
def step_impl_return(context, title):
    book = context.library.find_book(title)
    if book:
        book.is_on_loan = False

@then('I should find {count:d} book')
@then('I should find {count:d} books')
def step_impl_count(context, count):
    assert len(context.search_results) == count

@then('the book title should be "{title}"')
def step_impl_check_title(context, title):
    assert context.search_results[0].title == title

@then('"{title}" should be on loan')
def step_impl_is_loaned(context, title):
    book = context.library.find_book(title)
    assert book.is_on_loan is True

@then('"{title}" should not be on loan')
def step_impl_not_loaned(context, title):
    book = context.library.find_book(title)
    assert book.is_on_loan is False