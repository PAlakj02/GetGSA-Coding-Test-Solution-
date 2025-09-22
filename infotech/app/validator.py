import re
from app.models import CompanyProfile, ValidationResult

class Validator:
    def validate_company_profile(self, profile: CompanyProfile) -> ValidationResult:
        result = ValidationResult()
        
        # Check required fields
        if not profile.uei:
            result.issues.append("missing_uei")
        
        if not profile.poc_email:
            result.issues.append("missing_poc_email")
        elif not self._is_valid_email(profile.poc_email):
            result.issues.append("invalid_poc_email")
        
        if not profile.naics:
            result.issues.append("missing_naics")
        
        if not profile.company_name:
            result.issues.append("missing_company_name")
        
        if not profile.duns:
            result.issues.append("missing_duns")
        
        # Validate UEI format
        if profile.uei and not re.match(r'^[A-Z0-9]{12}$', profile.uei):
            result.issues.append("invalid_uei_format")
        
        # Validate DUNS format
        if profile.duns and not re.match(r'^\d{9}$', profile.duns):
            result.issues.append("invalid_duns_format")
        
        result.is_valid = len(result.issues) == 0
        return result
    
    def _is_valid_email(self, email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
