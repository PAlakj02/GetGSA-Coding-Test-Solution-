import pytest
from app.parser import TextParser

class TestParser:
    def test_missing_uei(self):
        parser = TextParser()
        text = """Acme Robotics LLC
DUNS: 123456789
NAICS: 541511, 541512
POC: Jane Smith, jane@acme.co, (415) 555-0100"""
        
        profile = parser.parse_company_profile(text)
        assert profile.uei is None
        assert profile.company_name == "Acme Robotics LLC"