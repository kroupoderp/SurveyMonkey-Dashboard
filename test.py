import re



x = r'<span style="color: #ffffff; font-size: 18pt;"><strong>This survey was created with the purpose of obtaining valuable information that can aid software developers in making key decisions about their careers and future. </strong></span>'




print(re.search("<span>*", x))