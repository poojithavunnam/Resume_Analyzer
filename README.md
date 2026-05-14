# Resume Analyzer

A Flask-based web application for analyzing resumes and matching skills against job requirements.

## Features

- Upload PDF resumes
- Extract text from PDF files
- Analyze skills against predefined job roles
- Calculate suitability score
- Display matched and missing skills
- User authentication and dashboard
- Resume history tracking

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLite
- **PDF Processing**: PyPDF2
- **Frontend**: HTML, CSS, Jinja2 templates
- **Session Management**: Flask-Session

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd MINI_Project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000`

## Usage

1. Register/Login to access the dashboard
2. Select a job role from the dropdown
3. Upload a PDF resume
4. View the analysis results including:
   - Extracted skills
   - Matched skills
   - Missing skills
   - Suitability percentage

## Project Structure

```
MINI_Project/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── models/
│   └── db.py             # Database models and connections
├── routes/
│   ├── auth_routes.py    # Authentication routes
│   ├── dashboard_routes.py # Dashboard routes
│   └── resume_routes.py  # Resume analysis routes
├── services/
│   ├── resume_service.py # Resume processing service
│   └── skill_service.py  # Skill analysis service
├── static/
│   └── style.css         # CSS styles
├── templates/
│   ├── dashboard.html    # Dashboard template
│   ├── index.html        # Main page template
│   └── login.html        # Login template
├── uploads/               # Uploaded resume files
└── utils/
    └── pdf_parser.py      # PDF text extraction utility
```

## Job Roles Supported

- SDE (Software Development Engineer)
- Data Scientist
- ML Engineer
- Web Developer

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.