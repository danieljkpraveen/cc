import re
from email import policy
from email.parser import BytesParser


def extract_email_body(eml_path):
    """Extracts the plain text body from a .eml file."""
    with open(eml_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                return part.get_content()
        for part in msg.walk():
            if part.get_content_type() == 'text/html':
                return part.get_content()
    else:
        return msg.get_content()
    return ""


def extract_rules(text):
    """Extract rules and their values from the email body."""
    pattern = r'(Rules where .*?=)\[(.*?)\]'
    matches = re.findall(pattern, text, re.DOTALL)
    extracted = []
    for rule_desc, values in matches:
        rule_desc = rule_desc.strip().rstrip('=').strip()
        value_list = [v.strip().strip('"').strip("'")
                      for v in values.split(',')]
        extracted.append([rule_desc] + value_list)
    return extracted
