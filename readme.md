# Web Scraper with GUI

This Python script provides a graphical user interface (GUI) for a web scraper that searches for specific terms on given URLs and extracts the sentences containing those terms.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Setup Instructions

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the project directory.

3. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```

5. Install the required packages:
   ```
   pip3 install scrapy beautifulsoup4
   ```

## Usage

1. Prepare two text files:
   - A file containing target URLs (one per line)
   - A file containing search terms (one per line)

2. Run the script:
   ```
   python3 web_scraper.py
   ```

3. In the GUI:
   - Click "Select URLs File" and choose your file with target URLs.
   - Click "Select Search Terms File" and choose your file with search terms.
   - Enter the minimum delay (in seconds) in the "Start delay" field.
   - Enter the maximum delay (in seconds) in the "Stop delay" field.
   - Click "Run Scraper" to start the process.

4. The script will create an output CSV file in the same directory, named in the format `SS.HH.MMoutput.csv` (where SS, HH, and MM are the current seconds, hours, and minutes, respectively).

5. Progress updates and any errors will be displayed in the terminal and through message boxes in the GUI.

## Notes

- Web scraping may be subject to legal and ethical considerations. Ensure you have the right to scrape the target websites and that you're not overloading their servers with requests.
- The script applies a random delay between requests based on the start and stop times you provide. This helps to avoid overwhelming the target servers.

## Troubleshooting

If you encounter any issues:

1. Ensure your virtual environment is activated.
2. Verify that all required packages are installed correctly.
3. Check that your input files (URLs and search terms) are formatted correctly, with one item per line.
4. Make sure you have an active internet connection.

If problems persist, check the error messages in the terminal or GUI for more information.

## Deactivating the Virtual Environment

When you're done using the script, you can deactivate the virtual environment by running:
```
deactivate
```

This will return you to your global Python environment.