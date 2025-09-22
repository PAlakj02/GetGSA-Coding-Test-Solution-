from dataclasses import dataclass, field
from typing import List, Optional
import uuid

@dataclass
class CompanyProfile:
    company_name: Optional[str] = None
    uei: Optional[str] = None
    duns: Optional[str] = None
    naics: List[str] = field(default_factory=list)
    poc_name: Optional[str] = None
    poc_email: Optional[str] = None
    poc_phone: Optional[str] = None
    address: Optional[str] = None
    sam_registered: Optional[bool] = None

@dataclass 
class PastPerformance:
    customer: Optional[str] = None
    contract: Optional[str] = None
    value: Optional[str] = None
    period: Optional[str] = None
    contact: Optional[str] = None

@dataclass
class ValidationResult:
    issues: List[str] = field(default_factory=list)
    is_valid: bool = True