# WebSecScanner

WebSecScanner is a simple command-line interface (CLI) tool designed to scan websites for basic security vulnerabilities. It analyzes HTTP headers, tests for basic Cross-Site Scripting (XSS) vulnerabilities, checks for HTTPS redirection and HTTP Strict Transport Security (HSTS), and generates a report listing any detected vulnerabilities.

## Features

- Analyze HTTP headers for security-related information.
- Test for basic XSS vulnerabilities.
- Check for HTTPS redirection.
- Verify HSTS implementation.
- Generate reports in markdown or text format.

## Installation

Since this project uses only standard Python libraries, no additional dependencies are required. You can clone the repository and run the tool directly.

```bash
git clone <repository-url>
cd WebSecScanner
```

## Usage

To use the WebSecScanner tool, run the following command:

```bash
python src/websecscanner.py <url>
```

Replace `<url>` with the website you want to scan.

## Reporting

The tool will generate a report detailing any vulnerabilities found during the scan. The report will be saved in the current directory in markdown format.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.