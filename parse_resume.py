from pyresparser.pyresparser.resume_parser import ResumeParser
import simplejson as json

data = ResumeParser('/Users/saif/Pictures/Gaurav_Resume.pdf').get_extracted_data()

print(json.dumps(data))