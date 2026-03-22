import pytest
from membership import Event, MemberService

pytestmark = pytest.mark.integration
# --- FIXTURES (Local to this file) ---
@pytest.fixture
def registration_setup():
    """Provides both objects needed for an integration flow."""
    return {
        "service": MemberService(),
        "event": Event("Workshop")
    }

# --- INTEGRATION TESTS ---
@pytest.mark.integration
def test_register_new_member_flow(registration_setup):
    """
    Verifies that register_new_member updates BOTH
    the MemberService and the Event list.
    """
    service = registration_setup["service"]
    event = registration_setup["event"]
    user_name = "Charlie"

    # Action: Trigger the coordination method
    event.register_new_member(user_name, service)

    # Assertions: Check both sides of the integration
    assert user_name in service.all_members, "Failed: User not in MemberService"
    assert user_name in event.registered_members, "Failed: User not in Event list"