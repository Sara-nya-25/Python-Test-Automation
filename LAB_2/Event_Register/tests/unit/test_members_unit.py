import pytest
from src.membership import Event, MemberService

print(dir(MemberService))
# --- FIXTURES (Local to this file) ---
@pytest.fixture
def member_service():
    return MemberService()

@pytest.fixture
def tech_event():
    return Event("Tech Meetup")

# --- UNIT TESTS ---
def test_sign_up_logic(tech_event):
    """Verifies sign_up writes a member to the event list."""
    result = tech_event.sign_up("Alice")
    assert result is True
    assert "Alice" in tech_event.registered_members


def test_add_member_spy(mocker, member_service):
    """Spies on MemberService.add_member to verify the call."""
    # We use mocker.spy to track the call while letting the real code run
    spy = mocker.spy(member_service, 'add_member')

    member_service.add_member("Bob")

    spy.assert_called_once_with("Bob")
    assert "Bob" in member_service.all_members




