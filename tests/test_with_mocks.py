"""
Tests that mock external API calls
"""

from unittest.mock import Mock, patch


def test_llm_call_mocked():
    """Test LLM call with mocked response"""
    # This doesn't actually call OpenAI!
    with patch("openai.ChatCompletion.create") as mock_create:
        # Set up the mock response
        mock_create.return_value = {
            "choices": [{"message": {"content": "Mocked response"}}]
        }

        # Your code would call this
        # response = call_llm("test")

        # Verify it was called
        # mock_create.assert_called_once()
        pass  # Adjust to your actual code


def test_text_classification_mock():
    """Test classification without actual model"""
    # Mock the classification
    ticket = "I need help with my order"

    # Simulate classification
    category = "order_issue"  # Would come from your model

    assert category in ["order_issue", "technical", "billing", "general"]
