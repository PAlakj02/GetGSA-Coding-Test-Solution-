import pytest
from app.validator import Validator
from app.models import CompanyProfile

class TestValidator:
    def test_invalid_email(self):
        validator = Validator()
        profile = CompanyProfile(
            company_name="Test Corp",
            uei="ABC123DEF456",
            poc_email="invalid-email"
        )
        
        result = validator.validate_company_profile(profile)
        assert "invalid_poc_email" in result.issues
        assert not result.is_valid