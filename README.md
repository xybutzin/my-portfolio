# Flask Portfolio Web Application

## Introduction
This project is a personal portfolio web application built using Flask. It hightlights my dual expertise as a microbiologist and a programmer. The portfolio serves as a professional online presence, showcasing my skills, projects, and providing ways for potential collaborators or employers to contact me. This project is part of my final class project for the CS50 course.

## Application Features

### Home Page
The home page introduces me as a microbiologist and programmer, featuring:
- **Profile Picture**: Positioned on the left to create a welcoming and personal touch.
- **Brief Introduction**: A concise overview of my background and expertise. 
- **Buttons**: Quick access to 
    1. **Download CV**: Provide a downloadable version of my CV.
    2. **GitHub profile**: Links to my GitHub repository showcasing projects.
    3. **LinkedIn profile**: Links to my professional LinkedIn profile.
    4. **Contact me**: Redirects visitors to the contact page

### About Page
The about page provides a brief professional biography, emphasizing my academic and technical background. A **button at the bottom** directs visitors to the projects page.

### Projects Page
This page showcases my programming projects:
- **GitHub Project Card**: Hightlights one of my repositories with a direct link to its GitHub page.
- The layout is designed to easily accommondate additional projects in the future.

### Skills Page
This page categorizes my expertise into four skill sets:
    1. **Python Skills**: Emphasizing data analysis, web development and machine learning.
    2. **Programming & Computational Skills**: Includes Linux command-line proficiency, HPC usage, R and SQL
    3. **Technical Skills**: Features RNA-seq analysis and molecular docking expertise.
    4. **Transferable Skills** Showcases problem-solving, data analysis, interdisciplinary knowledge, and communication.

Each skill set is displayed as a card for better visual appeal and clarity.

### Contact Page
The contact page provides a **user-friendly form** for visitors to send me messages. The form collects the send's name, email, and message, and delivers the information to my personal email account. Flask's backend ensures that the messages are processed securely. The form was implemented using Flask-WTF, and validation was handled by validators from wtforms.validators.

## Technical Details

### Frameworks and Libraries Used
- **Flask**: The primary web framework
- **HTML/CSS**: For structuring and styling the pages
- **Bootstrap**: To enhance responsiveness and design
- **Python Libraries**:
    - **Flask-WTF** for form validation.
    - **Flask-Mail** for handling email functionality, such as sending messages.
    - **dotenv** for securely handling sensitive configuration data through environement variables.

### Additional Features
- **Favicon**: A watermelon icon is used as a favicon to display in the page title, adding a personal and creative touch.

### Deployment

The application runs on a local Flask server for demonstration purposes and is deployed on Render for broader access (https://my-portfolio-jk4u.onrender.com/).

### Folder Structure

```
├── Procfile
├── README.md
├── __pycache__
│   ├── app.cpython-310.pyc
│   └── forms.cpython-310.pyc
├── app.py
├── forms.py
├── requirements.txt
├── runtime.txt
├── static
│   ├── Butzin_cv.pdf
│   ├── about.txt
│   ├── android-chrome-192x192.png
│   ├── android-chrome-512x512.png
│   ├── apple-touch-icon.png
│   ├── favicon-16x16.png
│   ├── favicon-32x32.png
│   ├── favicon.ico
│   ├── profile1.jpg
│   ├── site.webmanifest
│   └── styles.css 
└── templates
    ├── about.html
    ├── contact.html
    ├── index.html
    ├── layout.html
    ├── projects.html
    └── skills.html
```

### Security
Sensitive data (email credentials) is managed using environment variables.

### Additional considerations
- I debated adding a blogs page. While the blogs.html file is in place, I chose not to implement it because I wasn't sure how to prevent unauthorized users from uploading pages without implementing a registration function/route. This is a potential feature to explore in the future.

## Usage Guide

1. Clone the repository:
```
git clone https://github.com/xybutzin/my-portfolio.git
```
2. Navigate to the project directory:
```
cd my_portfolio
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Set up environment variables for Flask and email configuration.
5. Run the application
``` 
flask run
```
6. Open a browser and visit http://127.0.0.1:5000/ to view the portfolio.

