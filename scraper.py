import requests
from bs4 import BeautifulSoup
import csv

# Website URL (You can change this to another site if needed)
url = "https://books.toscrape.com/catalogue/page-1.html"

# Open a CSV file to save data
with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])

    # Loop through multiple pages (first 3 pages here)
    for page in range(1, 6):
        response = requests.get(f"https://books.toscrape.com/catalogue/page-{page}.html")
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all product containers
        products = soup.find_all("article", class_="product_pod")

        for product in products:
            # Extract product name
            name = product.h3.a["title"]

            # Extract product price
            price = product.find("p", class_="price_color").text

            # Extract product rating
            rating = product.p["class"][1]  # Example: "One", "Two", "Five"

            # Write row to CSV
            writer.writerow([name, price, rating])

print("✅ Data saved to products.csv")
