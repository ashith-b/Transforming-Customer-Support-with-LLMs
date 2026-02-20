"""
Simple tests for the customer support system
"""

import os


def test_requirements_exists():
    """Test that requirements.txt exists"""
    assert os.path.exists("requirements.txt"), "requirements.txt should exist"


def test_src_folder_exists():
    """Test that src folder exists"""
    assert os.path.exists("src"), "src folder should exist"


def test_helper_file_exists():
    """Test that helper.py exists"""
    assert os.path.exists("src/helper.py"), "src/helper.py should exist"


def test_demo_exists():
    """Test that demo.py exists"""
    assert os.path.exists("demo.py"), "demo.py should exist"


if __name__ == "__main__":
    # Run tests manually
    test_requirements_exists()
    test_src_folder_exists()
    test_helper_file_exists()
    test_demo_exists()
    print("✅ All tests passed!")
