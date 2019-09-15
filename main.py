import requests, json


access_token = 'xGXDyPakeNjQedIC4BTUQcgjknJ-MK-s.0x0Ap51iGOXnNHDjYPGDTkt6PSEycjqvlNEspmq0s2gbzkMXQnD.4n2AnQ9G2DsYjhaiFFYMCJcCM.87kITTBft8YHHCfOi'
url = "https://api.surveymonkey.com/v3/surveys?title=Canadian%20Vacation%20Preferences"


request_headers = {
    'Content-Type': "application/json",
    'Authorization': f'bearer {access_token}'
}


d = requests.get(url, headers=request_headers).text
json_frmt = json.loads(d)
print(json.dumps(json_frmt, indent=2))