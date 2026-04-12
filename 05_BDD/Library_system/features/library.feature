Feature: Library Management System

  Background:
    Given the library has the following books:
      | title          | author       |
      | The Hobbit     | J.R.R. Tolkien |
      | 1984           | George Orwell  |
      | Animal Farm    | George Orwell  |

  Scenario: Search for books by title
    When I search for books with title "1984"
    Then I should find 1 book
    And the book title should be "1984"

  Scenario: Search for books by author
    When I search for books by "George Orwell"
    Then I should find 2 books

  Scenario: Borrow a book
    When I borrow "The Hobbit"
    Then "The Hobbit" should be on loan

  Scenario: Return a book
    Given "The Hobbit" is currently on loan
    When I return "The Hobbit"
    Then "The Hobbit" should not be on loan