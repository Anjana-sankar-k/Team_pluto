import google.generativeai as genai
import os
from dotenv import load_dotenv
from datetime import datetime

class GeminiAstronomyClient:
    # """Client for fetching celestial information using Google's Gemini AI."""
    
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Configure Gemini
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable not found")
            
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def validate_date(self, date_str):
        """
        Validate and parse user input date.
        Accepts formats: YYYY-MM-DD, DD/MM/YYYY, MM/DD/YYYY
        """
        formats = [
            "%Y-%m-%d",
            "%d/%m/%Y",
            "%m/%d/%Y"
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
            except ValueError:
                continue
        raise ValueError("Invalid date format. Please use YYYY-MM-DD or DD/MM/YYYY or MM/DD/YYYY")
    
    def fetch_celestial_data(self, birth_date):
        """
        Fetch celestial event and constellation data for a birth date using Gemini.
        """
        try:
            # Validate and standardize date format
            formatted_date = self.validate_date(birth_date)
            
            # Construct the prompt for Gemini
            prompt = f"""
            For the date {formatted_date}, please provide:
            1. The constellation the Sun was in on that date
            2. An interesting astronomical fact related to that date or constellation
            
            Format the response as a JSON object with keys 'constellation' and 'fun_fact'.
            Keep the response concise and engaging.
            """
            
            # Get response from Gemini
            response = self.model.generate_content(prompt)
            
            try:
                content = response.text if hasattr(response, 'text') else response.parts[0].text
                
                # Clean up the response to get just the JSON part
                import json
                start = content.find('{')
                end = content.rfind('}') + 1
                if start >= 0 and end > start:
                    json_str = content[start:end]
                    data = json.loads(json_str)
                    return data
                else:
                    lines = content.split('\n')
                    constellation = next((line for line in lines if 'constellation' in line.lower()), "No constellation data found")
                    fun_fact = next((line for line in lines if 'fact' in line.lower()), "It was a great time to stargaze!")
                    return {
                        "constellation": constellation,
                        "fun_fact": fun_fact
                    }
                    
            except (json.JSONDecodeError, IndexError) as e:
                return {
                    "constellation": "Unable to parse constellation data",
                    "fun_fact": "Unable to parse astronomical fact"
                }
                
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}