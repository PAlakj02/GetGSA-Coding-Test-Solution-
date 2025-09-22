class NAICSMapper:
    NAICS_TO_SIN = {
        '541511': '54151S',
        '541512': '54151S', 
        '541611': '541611',
        '518210': '518210C'
    }
    
    def map_naics_to_sins(self, naics_codes: list) -> list:
        sins = []
        for code in naics_codes:
            if code in self.NAICS_TO_SIN:
                sin = self.NAICS_TO_SIN[code]
                if sin not in sins:  # Avoid duplicates
                    sins.append(sin)
        return sins