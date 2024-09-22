import tkinter as tk
from tkinter import filedialog, messagebox
import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
import csv
import random
import time
from datetime import datetime
import os

class WebScraper(scrapy.Spider):
    name = 'web_scraper'

    def __init__(self, urls, search_terms, start_time, stop_time, *args, **kwargs):
        super(WebScraper, self).__init__(*args, **kwargs)
        self.urls = urls
        self.search_terms = search_terms
        self.start_time = start_time
        self.stop_time = stop_time
        self.output_file = f"{datetime.now().strftime('%S.%H.%M')}output.csv"
        
        with open(self.output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['URL', 'SEARCHTERM', 'SENTENCE'])

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        for search_term in self.search_terms:
            sentences = soup.find_all(string=lambda text: search_term.lower() in text.lower())
            for sentence in sentences:
                full_sentence = ' '.join(sentence.strip().split())  # Preserve whitespace, remove tabs and newlines
                with open(self.output_file, 'a', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([response.url, search_term, full_sentence])
                print(f"Found '{search_term}' in {response.url}")
        
        # Random delay between requests
        delay = random.uniform(self.start_time, self.stop_time)
        time.sleep(delay)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Web Scraper")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.url_button = tk.Button(self)
        self.url_button["text"] = "Select URLs File"
        self.url_button["command"] = self.select_urls_file
        self.url_button.pack(side="top")

        self.url_label = tk.Label(self, text="No file selected")
        self.url_label.pack(side="top")

        self.term_button = tk.Button(self)
        self.term_button["text"] = "Select Search Terms File"
        self.term_button["command"] = self.select_terms_file
        self.term_button.pack(side="top")

        self.term_label = tk.Label(self, text="No file selected")
        self.term_label.pack(side="top")

        self.start_label = tk.Label(self, text="Start delay (seconds):")
        self.start_label.pack(side="top")
        self.start_entry = tk.Entry(self)
        self.start_entry.insert(0, "5")  # Default value
        self.start_entry.pack(side="top")

        self.stop_label = tk.Label(self, text="Stop delay (seconds):")
        self.stop_label.pack(side="top")
        self.stop_entry = tk.Entry(self)
        self.stop_entry.insert(0, "10")  # Default value
        self.stop_entry.pack(side="top")

        self.run_button = tk.Button(self)
        self.run_button["text"] = "Run Scraper"
        self.run_button["command"] = self.run_scraper
        self.run_button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        # Set default file paths
        self.urls_file = "/home/dgd/Documents/scrapy_search/searchurls.txt"
        self.terms_file = "/home/dgd/Documents/scrapy_search/searchterms.txt"
        
        # Update labels with default file names
        self.update_url_label()
        self.update_term_label()

    def select_urls_file(self):
        self.urls_file = filedialog.askopenfilename(initialdir="/home/dgd/Documents/scrapy_search/",
                                                    initialfile="searchurls.txt")
        self.update_url_label()

    def select_terms_file(self):
        self.terms_file = filedialog.askopenfilename(initialdir="/home/dgd/Documents/scrapy_search/",
                                                     initialfile="searchterms.txt")
        self.update_term_label()

    def update_url_label(self):
        self.url_label.config(text=os.path.basename(self.urls_file))

    def update_term_label(self):
        self.term_label.config(text=os.path.basename(self.terms_file))

    def run_scraper(self):
        try:
            with open(self.urls_file, 'r') as f:
                urls = [line.strip() for line in f]

            with open(self.terms_file, 'r') as f:
                search_terms = [line.strip() for line in f]

            start_time = float(self.start_entry.get())
            stop_time = float(self.stop_entry.get())

            process = CrawlerProcess()
            process.crawl(WebScraper, urls=urls, search_terms=search_terms, 
                          start_time=start_time, stop_time=stop_time)
            process.start()

            messagebox.showinfo("Success", "Scraping completed!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
app = Application(master=root)
app.mainloop()