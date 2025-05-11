# GitHubUserDataExtractor

**GitHubUserDataExtractor** is a cross-platform Python tool designed to extract and display public GitHub user data both in the terminal and through a visual HTML dashboard. It provides a streamlined way to fetch a user’s profile, recent activity, and contribution statistics using GitHub’s REST API and external visualization services.

## Features

- Retrieves a GitHub user's public profile and recent activity
- Displays formatted JSON data in the terminal with color-coded output
- Generates a dynamic HTML dashboard styled with Bootstrap
- Embeds contribution graphs, language usage charts, and GitHub stats
- Native HTML viewer support for Linux (PyWebView) and Windows (PyQt5)
- Clean file structure with modular code organization

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/QuantumByteStudios/GitHubUserDataExtractor.git
cd GitHubUserDataExtractor
pip install -r requirements.txt
```

Ensure you are using Python 3.7 or higher.

## Usage

Run the application using:

```bash
python src/main.py
```

You will be prompted to enter a GitHub username. The tool will:

1. Fetch the user's public GitHub profile and display it in the terminal.
2. Retrieve recent events like stars, forks, and releases.
3. Generate an HTML report and open it in a native desktop viewer.
4. Clean up temporary files after closing the viewer.

Runtime Screenshot

## Project Structure

```
GitHubUserDataExtractor/
│
├── src/
│   ├── cli/                   # Terminal input/output logic
│   ├── core/                  # API and HTML generation logic
│   └── ui/htmlviewers/        # Platform-specific GUI viewers
│
├── assets/
│   └── templates/             # HTML/CSS/JS templates
│
├── tests/                     # Unit tests
├── requirements.txt
├── README.md
```

## Output

The tool creates a temporary HTML report (`index.html`) inside the `assets/output/` directory. This report includes:

- Recent GitHub events (filtered by event types)
- Contribution graphs and language usage charts
- Visual badges and statistics via third-party services

This file is opened in a native GUI window and then automatically cleared on exit.

## Use Cases

- Developers reviewing their own GitHub contributions and stats
- Technical recruiters assessing candidate GitHub activity
- Educators demonstrating API integration and data visualization
- Hackathon teams building offline GitHub user snapshots

## Technologies

- Python 3
- GitHub REST API
- Requests (HTTP client)
- Colorama (terminal color formatting)
- PyQt5 (Windows HTML viewer)
- PyWebView (Linux HTML viewer)
- Bootstrap 5 (UI styling)
- External visualization APIs:
  - GitHub Readme Stats
  - GitHub Streak Stats
  - GitHub Profile Summary Cards

## API Limitations

This tool uses unauthenticated GitHub API requests and is therefore subject to rate limiting:

- 60 requests per hour per IP address

To increase limits, you can optionally extend the tool to use a personal access token.

## License

This project is licensed under the MIT License. See `LICENSE.md` for details.

## Author

Developed by QuantumByteStudios. Contributions and suggestions are welcome.  
For inquiries, email us at [contact@quantumbytestudios.in](mailto:contact@quantumbytestudios.in).
