# Project Title: Article Scraper and Viewer

## Description
This project is a web application that scrapes articles from a specified website and stores them in a MongoDB database. The application features a user-friendly interface that displays the articles, styled with CSS and enhanced with JavaScript for dynamic content loading.

## Project Structure
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

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd project-folder
   ```

2. **Install dependencies**:
   Ensure you have Python and pip installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Set up MongoDB**:
   Make sure you have a MongoDB instance running. Update the connection string in `scraper.py` and `app.py` as needed.

4. **Run the scraper**:
   Execute the scraper to fetch articles:
   ```
   python scraper.py
   ```

5. **Start the web server**:
   Run the application:
   ```
   python app.py
   ```

6. **Access the application**:
   Open your web browser and go to `http://localhost:5000` to view the articles.

## Usage
- The application will display the latest articles fetched from the specified website.
- Articles are stored in the MongoDB database, ensuring that only new articles are added during each scrape.

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License.