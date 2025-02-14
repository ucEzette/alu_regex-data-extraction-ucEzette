import re

# List of valid HTML tags
valid_tags = [
        'a', 'abbr', 'address', 'area', 'article', 'aside', 'audio', 'b', 'base', 'bdi', 'bdo', 'blockquote', 'body',
        'br', 'button', 'canvas', 'caption', 'cite', 'code', 'col', 'colgroup', 'data', 'datalist', 'dd', 'del',
        'details', 'dfn', 'dialog', 'div', 'dl', 'dt', 'em', 'embed', 'fieldset', 'figcaption', 'figure', 'footer',
        'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hr', 'html', 'i', 'iframe', 'img', 'input',
        'ins', 'kbd', 'label', 'legend', 'li', 'link', 'main', 'map', 'mark', 'meta', 'meter', 'nav', 'noscript',
        'object', 'ol', 'optgroup', 'option', 'output', 'p', 'param', 'picture', 'pre', 'progress', 'q', 'rp', 'rt',
        'ruby', 's', 'samp', 'script', 'section', 'select', 'small', 'source', 'span', 'strong', 'style', 'sub',
        'summary', 'sup', 'table', 'tbody', 'td', 'template', 'textarea', 'tfoot', 'th', 'thead', 'time', 'title',
        'tr', 'track', 'u', 'ul', 'var', 'video', 'wbr']

# Function to load sample text from a file
def load_sample_text(filename):
    with open(filename, 'r') as file:
        return file.read()

# 1. Extracting Email Addresses
def extract_emails (text):
    email_pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)
# 2. Extracting URLs
def extract_urls(text):
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    return re.findall(url_pattern, text)

# 3. Extracting Phone Numbers (various formats)
def extract_phone_numbers(text):
    phone_pattern = r'(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}'
    return re.findall(phone_pattern, text)

# 4. Extracting Time in 12-hour or 24-hiour format
def extract_times(text):
    time_pattern =  r'\b(?:[01][0-9]|2[0-3]):[0-5][0-9]\b|(?:0?[1-9]|1[0-2]):[0-5][0-9] ?(?:AM|PM)\b'
    return re.findall(time_pattern, text)
# 5. Extracting Hashtags
def extract_hashtags(text):
    hashtag_pattern =r'#\w+'
    return re.findall(hashtag_pattern, text)
# 6. Extracting Credit Card Numbers
def extract_credit_cards(text):
    credit_card_pattern = r'(\d{4}[-\s]?){3}\d{4}'
    return re.findall(credit_card_pattern, text)

# 7. Extracting HTML Tags
import re

def extract_html_tags(text):
    
    # Regular expression pattern to match valid HTML tags
    html_tag_pattern = r'</?(' + '|'.join(valid_tags) + r')(?:\s+[a-zA-Z\-]+(?:\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^\s>]+))?)*\s*/?>'
    
    # Find all matches of the pattern in the text
    return re.findall(html_tag_pattern, text)

# 8. Extracting Currency Amounts
def extract_currency_amounts(text):
    currency_pattern = r'(?<!\w)([$€£¥₹])?\s?(-?\d{1,3}(,\d{3})*(\.\d{2})?)(?!\w)'
    return re.findall(currency_pattern, text)
# Main function to load the text and run the extractions
def main():
    # Load the sample text from the file
    data_sample = load_sample_text('data_sample.txt')

    # Extract and print different types of data
    print()
    print("=========================")
    print("Extracted Data")
    print("=========================")
    print()
    print("Extracted Email Addresses:", extract_emails(data_sample))
    print()
    print("Extracted URLs:", extract_urls(data_sample))
    print()
    print("Extracted Phone Numbers:", extract_phone_numbers(data_sample))
    print()
    print("Extracted Times:", extract_times(data_sample))
    print()
    print("Extracted Hashtags:", extract_hashtags(data_sample))
    print()
    print("Extracted Credit Card Numbers:", extract_credit_cards(data_sample))
    print()
    print("Extracted HTML Tags:", extract_html_tags(data_sample))
    print()
    print("Extracted Currency Amounts:", extract_currency_amounts(data_sample))
    print()

if __name__ == '__main__':
    main()
