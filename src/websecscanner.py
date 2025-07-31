import requests

def check_https_redirection(url):
    try:
        response = requests.get(url, allow_redirects=False)
        if response.status_code in (301, 302):
            redirect_url = response.headers.get('Location')
            if redirect_url.startswith('https://'):
                return True, redirect_url
            else:
                return False, redirect_url
        return False, None
    except requests.RequestException as e:
        return False, str(e)

def check_hsts(url):
    try:
        response = requests.get(url)
        hsts = response.headers.get('Strict-Transport-Security')
        return hsts is not None, hsts
    except requests.RequestException as e:
        return False, str(e)

def analyze_http_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        return headers
    except requests.RequestException as e:
        return str(e)

def test_xss(url):
    payload = "<script>alert('XSS')</script>"
    try:
        response = requests.get(url + "?search=" + payload)
        if payload in response.text:
            return True
        return False
    except requests.RequestException as e:
        return str(e)

def generate_report(url):
    report = f"# Security Report for {url}\n\n"
    
    # Check HTTPS redirection
    https_redirect, redirect_url = check_https_redirection(url)
    report += f"## HTTPS Redirection: {'Yes' if https_redirect else 'No'}\n"
    if redirect_url:
        report += f"Redirect URL: {redirect_url}\n\n"
    
    # Check HSTS
    hsts, hsts_value = check_hsts(url)
    report += f"## HSTS: {'Yes' if hsts else 'No'}\n"
    if hsts_value:
        report += f"HSTS Value: {hsts_value}\n\n"
    
    # Analyze HTTP headers
    headers = analyze_http_headers(url)
    report += "## HTTP Headers:\n"
    if isinstance(headers, dict):
        for key, value in headers.items():
            report += f"- **{key}**: {value}\n"
    else:
        report += headers + "\n"
    
    # Test for XSS
    xss_vulnerable = test_xss(url)
    report += f"## XSS Vulnerability: {'Yes' if xss_vulnerable else 'No'}\n"
    
    return report

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Web Security Scanner')
    parser.add_argument('url', type=str, help='The URL of the website to scan')
    parser.add_argument('--report', type=str, help='Output report file name', default='report.md')

    args = parser.parse_args()
    report = generate_report(args.url)

    with open(args.report, 'w') as f:
        f.write(report)

    print(f"Report generated: {args.report}")