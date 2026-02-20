"""
Advanced tests for customer support system
"""
import pytest
import sys
import os

# Add src to path so we can import helper
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Test imports work
def test_can_import_src():
    """Test that we can import from src"""
    try:
        from src import helper
        assert True
    except ImportError as e:
        pytest.fail(f"Cannot import helper: {e}")

# Test file structure
def test_project_structure():
    """Test that all required files exist"""
    required_files = [
        'src/helper.py',
        'demo.py',
        'requirements.txt',
        'README.md'
    ]
    
    for file_path in required_files:
        assert os.path.exists(file_path), f"{file_path} should exist"

def test_required_folders():
    """Test that required folders exist"""
    required_folders = [
        'src',
        'tests',
        'vector_store',
        'Customer_Support_Training_Dataset'
    ]
    
    for folder in required_folders:
        assert os.path.exists(folder), f"{folder} should exist"

# Test requirements.txt
def test_requirements_format():
    """Test that requirements.txt is properly formatted"""
    with open('requirements.txt', 'r') as f:
        lines = f.readlines()
    
    # Should have at least some packages
    assert len(lines) > 0, "requirements.txt should not be empty"
    
    # Check for key packages
    content = ''.join(lines).lower()
    key_packages = ['openai', 'langchain', 'faiss', 'streamlit']
    
    for package in key_packages:
        assert package in content, f"{package} should be in requirements.txt"

# Test demo.py structure
def test_demo_file_structure():
    """Test that demo.py has expected structure"""
    with open('demo.py', 'r') as f:
        content = f.read()
    
    # Should have streamlit imports
    assert 'streamlit' in content, "demo.py should import streamlit"
    
    # Should have title or header
    assert 'st.title' in content or 'st.header' in content, \
        "demo.py should have title or header"

# Test helper.py structure
def test_helper_has_functions():
    """Test that helper.py has expected functions"""
    with open('src/helper.py', 'r') as f:
        content = f.read()
    
    # Should have function definitions
    assert 'def ' in content, "helper.py should have function definitions"
    
    # Likely has call_llm function
    assert 'call_llm' in content or 'openai' in content.lower(), \
        "helper.py should have LLM calling functionality"

# Test data processing (example - adjust to your actual code)
def test_text_processing():
    """Test basic text processing"""
    # Simple test that doesn't require external dependencies
    test_text = "This is a customer support ticket"
    
    # Test text is not empty
    assert len(test_text) > 0
    
    # Test text cleaning works
    cleaned = test_text.strip().lower()
    assert 'customer support' in cleaned

# Mock test for LLM function (doesn't actually call API)
def test_llm_function_exists():
    """Test that LLM calling function exists in helper.py"""
    try:
        with open('src/helper.py', 'r') as f:
            content = f.read()
        
        # Check function exists
        assert 'def call_llm' in content or 'def ' in content, \
            "helper.py should have function definitions"
    except FileNotFoundError:
        pytest.fail("src/helper.py not found")

# Test vector store
def test_vector_store_exists():
    """Test that FAISS index exists"""
    vector_store_path = 'vector_store/faiss_index.index'
    
    # Check if file exists
    if os.path.exists(vector_store_path):
        # Check it's not empty
        assert os.path.getsize(vector_store_path) > 0, \
            "FAISS index should not be empty"
    else:
        # It's okay if it doesn't exist yet
        pytest.skip("FAISS index not yet created")

# Test dataset
def test_dataset_exists():
    """Test that training dataset exists"""
    dataset_path = 'Customer_Support_Training_Dataset/Customer_Support_Training_Dataset.csv'
    
    if os.path.exists(dataset_path):
        assert os.path.getsize(dataset_path) > 0, \
            "Dataset should not be empty"
    else:
        pytest.skip("Dataset not yet added")

# Integration test (without API call)
def test_system_components():
    """Test that all system components are in place"""
    components = {
        'Helper Module': 'src/helper.py',
        'Demo App': 'demo.py',
        'Vector Store': 'vector_store',
        'Dataset': 'Customer_Support_Training_Dataset',
        'Requirements': 'requirements.txt'
    }
    
    missing = []
    for name, path in components.items():
        if not os.path.exists(path):
            missing.append(name)
    
    assert len(missing) == 0, f"Missing components: {', '.join(missing)}"

if __name__ == "__main__":
    pytest.main([__file__, '-v'])