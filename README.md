# Assignment_5_web_scraping


Methodology Overview
Web Scraping (Using Selenium)

Headless Chrome browser is used to scrape eBay's tech deals.
Dynamic content loading is handled by scrolling until all products are visible.
User-Agent rotation is implemented to reduce the risk of detection.
Explicit waits (WebDriverWait) are used to ensure elements load before extraction.
The scraped data includes:
Timestamp
Product title
Current price & original price
Shipping information
Product URL
Data Cleaning (Using Pandas)

Prices are converted to numerical format for analysis.
Missing original prices are replaced with the current price.
Shipping info is standardized (e.g., replacing empty values with "Shipping info unavailable").
Discount percentages are calculated.
Automated Workflow (GitHub Actions)

The scraper runs every 3 hours using a cron job.
The scraped data is committed and pushed to a GitHub repository.
Challenges Faced
Risk of IP Blocking / Detection

eBay might detect Selenium-based scraping, leading to CAPTCHAs or IP bans.
Current approach rotates User-Agent, but additional precautions (e.g., proxy usage) may be needed.
Page Load & Scrolling Issues

Scroll-to-load might not always fetch all products.
Some elements may load late, leading to incomplete data.
Duplicate Entries Over Time

Since the scraper runs every 3 hours, duplicate entries can occur in the CSV.
Handling Missing or Inconsistent Data

Some items might be out of stock or no longer available, causing missing data.
Different currency formats (if eBay shows localized prices) could require extra processing.
Potential Improvements
Optimize Scraping Strategy

Implement rotating proxies to avoid IP bans.
Enhance Data Storage & Versioning

Instead of appending to CSV we might use:
A database (SQLite, PostgreSQL) for structured storage.
A hash-based de-duplication check before saving new records.
Improve Data Quality

Implement error handling/logging to track failed extractions.
