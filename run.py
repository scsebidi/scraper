from scrapy import cmdline

def main():
    cmdline.execute(f"scrapy runspider app.py".split())

if __name__ == "__main__":
   main()
