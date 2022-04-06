from website_scraper import Website_Scrapper
def main():
    ws = Website_Scrapper()
    ws.driver.close()

if __name__ == "__main__":
    main()