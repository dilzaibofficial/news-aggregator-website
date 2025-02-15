# 🚀 Dil Zaib's Project

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?lines=Hi+Guys!;I'm+Dil+Zaib!&font=Fira%20Code&center=true&width=380&height=50">
</p>

## 📌 Project Structure
```
project-folder
├── scraper.py          # Contains the web scraping logic
├── templates
│   └── index.html     # Main HTML template for the website
├── static
│   ├── css
│   │   └── styles.css  # CSS styles for the website
│   └── js
│       └── scripts.js   # JavaScript code for dynamic content
├── app.py             # Main application file for the web server
├── requirements.txt    # Lists project dependencies
└── README.md           # Project documentation
```

## 📸 Project Preview
Below are some previews of the application:

![Project Preview](Preview/newsAggregator.gif)

## 🛠 Tech Stack

<div align="center" style="display: inline_block"><br>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" alt="flask" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" alt="mongodb" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" alt="git" width="40" height="40"/>
</div>

## 📌 Features

- Scrapes articles from multiple news channels (Geo News, BOL News, SAMAA News)
- Displays articles with pagination
- Navigation bar to switch between different news channels
- Responsive design with Bootstrap

## 📌 Frontend (HTML, CSS, JavaScript)

- **HTML Files**
  - `index.html`: Main page displaying the articles with pagination and navigation bar.
- **CSS Files**
  - `styles.css`: Styles for the main page and articles.
- **JavaScript Files**
  - `scripts.js`: Handles fetching articles from the server and updating the DOM.

## 📌 Backend (Python with Flask)

- **Scraper**
  - `scraper.py`: Scrapes articles from Geo News, BOL News, and SAMAA News and stores them in MongoDB.
- **Flask App**
  - `app.py`: Sets up the Flask server, connects to MongoDB, and serves the articles with pagination.
- **Routes**
  - `/api/articles/<channel>`: Fetches articles from the specified news channel with pagination.

## 💻 How to Run the Project

1. Clone the repository:
   ```sh
   git clone https://github.com/dilzaibofficial/news-aggregator-website.git
   ```
2. Navigate to the project folder and install dependencies:
   ```sh
   cd news-aggregator-website
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```sh
   python app.py
   ```

## 📡 Connect with Me
<div align="center">
  <a href="https://dilzaibofficial.github.io/" target="_blank"><img src="https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white" target="_blank"></a>
  <a href="https://www.linkedin.com/in/dilzaibofficial" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
  <a href="https://x.com/dilzaibofficial" target="_blank"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" target="_blank"></a>
  <a href="https://www.instagram.com/dilzaibofficial" target="_blank"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a>
  <a href="https://youtube.com/@dilzaibofficial" target="_blank"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" target="_blank"></a>
  <a href="https://www.facebook.com/share/165J8YXU5k/" target="_blank"><img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" target="_blank"></a>
</div>

---
🎯 **Dil Zaib** | [GitHub](https://github.com/dilzaibofficial) | Passionate Developer 🚀