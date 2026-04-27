import re
from playwright.sync_api import Page, expect

BASE_URL = "https://lejonmanen.github.io/agile-helper/"

def test_sprint_planning_flow(page: Page):
    """User Story: Access Sprint Planning (First Day)"""
    page.goto(BASE_URL)

    english_btn = page.locator('[data-testid="language-en"]')
    english_btn.click()
    # Click "First" phase
    page.get_by_role("button", name="First").click()

    # Click "Sprint planning"
    page.get_by_role("button", name=re.compile("Sprint planning", re.IGNORECASE)).click()

    # Verify Dialog and Heading
    ceremony_container = page.locator(".sprint-ceremony.dialog.show")
    expect(ceremony_container).to_be_visible()
    expect(ceremony_container).to_contain_text("Sprint planning")

def test_daily_standup_flow(page: Page):
    """User Story: Access Daily Standup (Middle of Sprint)"""
    page.goto(BASE_URL)
    english_btn = page.locator('[data-testid="language-en"]')
    english_btn.click()
    page.get_by_role("button", name=re.compile("middle", re.IGNORECASE)).click()
    page.get_by_role("button", name=re.compile("Daily Standup", re.IGNORECASE)).click()

    ceremony_container = page.locator(".sprint-ceremony.dialog.show")
    expect(ceremony_container).to_be_visible(timeout=7000)
    expect(ceremony_container).to_contain_text(re.compile("daily standup", re.IGNORECASE))
    # Implicitly test that the standup content is loaded
    expect(ceremony_container).to_contain_text("What have you done since last standup?")


def test_retrospective_flow(page: Page):
    """User Story: Access Sprint Retrospective (Last Day)"""
    page.goto(BASE_URL)
    english_btn = page.locator('[data-testid="language-en"]')
    english_btn.click()
    page.get_by_role("button", name="Last").click()
    page.get_by_role("button", name="Sprint Retrospective").click()

    expect(page.get_by_role("heading", name="Sprint Retrospective")).to_be_visible()

