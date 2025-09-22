import re
from app.models import CompanyProfile, PastPerformance

class TextParser:
    def parse_company_profile(self, text: str) -> CompanyProfile:
        profile = CompanyProfile()
        
        lines = text.strip().split('\n')
        
        # Company name is usually first line
        if lines:
            profile.company_name = lines[0].strip()
        
        # Extract UEI
        uei_match = re.search(r'UEI:\s*([A-Z0-9]{12})', text, re.IGNORECASE)
        if uei_match:
            profile.uei = uei_match.group(1)
        
        # Extract DUNS
        duns_match = re.search(r'DUNS:\s*(\d{9})', text)
        if duns_match:
            profile.duns = duns_match.group(1)
        
        # Extract NAICS codes
        naics_match = re.search(r'NAICS:\s*([\d,\s]+)', text)
        if naics_match:
            naics_str = naics_match.group(1)
            profile.naics = [code.strip() for code in naics_str.split(',')]
        
        # Extract POC info
        poc_match = re.search(r'POC:\s*([^,]+),\s*([^,]+),\s*(.+)', text)
        if poc_match:
            profile.poc_name = poc_match.group(1).strip()
            profile.poc_email = poc_match.group(2).strip()
            profile.poc_phone = poc_match.group(3).strip()
        
        # Extract address
        addr_match = re.search(r'Address:\s*(.+)', text)
        if addr_match:
            profile.address = addr_match.group(1).strip()
        
        # Extract SAM registration
        sam_match = re.search(r'SAM\.gov:\s*(registered|active)', text, re.IGNORECASE)
        if sam_match:
            profile.sam_registered = True
        
        return profile
    
    def parse_past_performance(self, text: str) -> PastPerformance:
        performance = PastPerformance()
        
        # Extract customer
        customer_match = re.search(r'Customer:\s*(.+)', text)
        if customer_match:
            performance.customer = customer_match.group(1).strip()
        
        # Extract contract
        contract_match = re.search(r'Contract:\s*(.+)', text)
        if contract_match:
            performance.contract = contract_match.group(1).strip()
        
        # Extract value
        value_match = re.search(r'Value:\s*(.+)', text)
        if value_match:
            performance.value = value_match.group(1).strip()
        
        # Extract period
        period_match = re.search(r'Period:\s*(.+)', text)
        if period_match:
            performance.period = period_match.group(1).strip()
        
        # Extract contact
        contact_match = re.search(r'Contact:\s*(.+)', text)
        if contact_match:
            performance.contact = contact_match.group(1).strip()
        
        return performance
