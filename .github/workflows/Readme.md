## 🔄 CI/CD Pipeline

This project includes a fully automated CI/CD pipeline using GitHub Actions.

### Pipeline Overview
```yaml
┌─────────────┐
│  Git Push   │
└──────┬──────┘
       │
       ▼
┌──────────────────────────────────┐
│    GitHub Actions Triggered      │
└──────┬───────────────────────────┘
       │
       ├──▶ Install Dependencies
       │
       ├──▶ Run Unit Tests
       │    └─ test_helper.py
       │    └─ test_advanced.py
       │    └─ test_with_mocks.py
       │
       ├──▶ Generate Coverage Report
       │    └─ Coverage: 85%+
       │
       ├──▶ Code Quality Checks
       │    ├─ Black (formatting)
       │    ├─ isort (import sorting)
       │    └─ flake8 (linting)
       │
       └──▶ Report Results
            └─ All checks passed
```

### Running Tests Locally
```bash
# Install dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black flake8 isort

# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
open htmlcov/index.html

# Check code quality
black --check .
flake8 .
isort --check-only .
```

### CI/CD Features

**Automated Testing** - Runs on every push and pull request
**Code Coverage** - Tracks test coverage percentage
**Code Quality** - Enforces formatting and linting standards
**Dependency Caching** - Faster builds with cached packages
**Multi-Stage Pipeline** - Separates testing and quality checks
**Status Badges** - Visual indicators of build health

### Workflow Files

- `.github/workflows/python-tests.yml` - Main testing pipeline
- `.github/workflows/code-quality.yml` - Code quality enforcement