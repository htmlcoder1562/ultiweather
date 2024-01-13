try:
    import requests
except:
    import os
    os.system("pip3 install requests")
    import requests
class weather:
    def __init__(self, api_key, zip_code):
        self.key=api_key
        self.zip=zip_code
    def get(self, quality_of_air="no"):
        api_key=self.key
        zip_code=self.zip
        url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={zip_code}&aqi={quality_of_air}'

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                temperature = data['current']['temp_f']
                condition = data['current']['condition']['text']
                updated_time=data['current']['last_updated']

                return f'Current temperature in {zip_code}: {int(temperature)}°F, {condition} and updated at: {updated_time}.'
            else:
                return f'Failed to retrieve weather information. Status code: {response.status_code}'
        except Exception as e:
            return f'An error occurred: {str(e)}'