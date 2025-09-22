from flask import Blueprint, request, jsonify
import uuid
import logging
from app.parser import TextParser
from app.validator import Validator
from app.mapper import NAICSMapper

api_bp = Blueprint('api', __name__)

@api_bp.route('/ingest', methods=['POST'])
def ingest():
    try:
        # Generate request ID
        request_id = str(uuid.uuid4())
        
        # Get input data
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        company_text = data.get('company_profile', '')
        performance_text = data.get('past_performance', '')
        
        # Initialize components
        parser = TextParser()
        validator = Validator()
        mapper = NAICSMapper()
        
        # Parse company profile
        company_profile = parser.parse_company_profile(company_text)
        past_performance = parser.parse_past_performance(performance_text)
        
        # Validate
        validation_result = validator.validate_company_profile(company_profile)
        
        # Map NAICS to SINs
        recommended_sins = mapper.map_naics_to_sins(company_profile.naics)
        
        # Build checklist
        checklist = {
            "has_uei": bool(company_profile.uei),
            "has_valid_email": bool(company_profile.poc_email) and validator._is_valid_email(company_profile.poc_email or ""),
            "has_naics": len(company_profile.naics) > 0,
            "has_past_performance": bool(past_performance.customer),
            "has_duns": bool(company_profile.duns),
            "sam_registered": bool(company_profile.sam_registered)
        }
        checklist["required_ok"] = all([
            checklist["has_uei"],
            checklist["has_valid_email"], 
            checklist["has_naics"]
        ])
        
        # Build response
        response = {
            "request_id": request_id,
            "parsed": {
                "company_name": company_profile.company_name,
                "uei": company_profile.uei,
                "duns": company_profile.duns,
                "naics": company_profile.naics,
                "poc_name": company_profile.poc_name,
                "poc_email": company_profile.poc_email,
                "poc_phone": company_profile.poc_phone,
                "address": company_profile.address,
                "sam_registered": company_profile.sam_registered,
                "past_performance": {
                    "customer": past_performance.customer,
                    "contract": past_performance.contract,
                    "value": past_performance.value,
                    "period": past_performance.period,
                    "contact": past_performance.contact
                }
            },
            "issues": validation_result.issues,
            "recommended_sins": recommended_sins,
            "checklist": checklist
        }
        
        # Log audit trail
        logging.info(f"Request {request_id}: Validation issues: {validation_result.issues}, Required OK: {checklist['required_ok']}")
        
        return jsonify(response), 200
        
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500