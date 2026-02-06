import pandas as pd
import sqlite3
conn = sqlite3.connect("data.sqlite")

# products table
print(pd.read_sql("""
SELECT *
  FROM products;
""", conn))
print("\n")

# Ordered by the product name
print(pd.read_sql("""
SELECT *
  FROM products
 ORDER BY productName;
""", conn))
print("\n")

# Alternate way to order specifying ASC explicitly (it will be the same result)
print(pd.read_sql("""
SELECT *
  FROM products
 ORDER BY productName ASC;
""", conn))
print("\n")

# Ordered by product name in descending order
print(pd.read_sql("""
SELECT *
  FROM products
 ORDER BY productName DESC;
""", conn))
print("\n")

# Ordered by the length of the product description
print(pd.read_sql("""
SELECT productName, length(productDescription) AS description_length
  FROM products
 ORDER BY description_length;
""", conn))
print("\n")

# We can also sort by something without selecting it.
# Here is a query that has the same order as the query above, but doesn't select the description length
print(pd.read_sql("""
SELECT productName
  FROM products
 ORDER BY length(productDescription);
""", conn))
print("\n")


# Sort by productVendor and then by productName
print(pd.read_sql("""
SELECT productVendor, productName, MSRP
  FROM products
 ORDER BY productVendor, productName;
""", conn))
print("\n")

# Sort by productName and then by productVendor
print(pd.read_sql("""
SELECT productVendor, productName, MSRP
  FROM products
 ORDER BY productName, productVendor;
""", conn))
print("\n")

# Count distinct product vendors and product names
print(pd.read_sql("""
SELECT COUNT(DISTINCT productVendor) AS num_product_vendors,
       COUNT(DISTINCT productName) AS num_product_names
  FROM products;
""", conn))
print("\n")

# Order by quantityInStock. It's not good because quantities are strings
print(pd.read_sql("""
SELECT productName, quantityInStock
  FROM products
 ORDER BY quantityInStock;
""", conn))
print("\n")

# Same as above, but getting the first 10 rows
print(pd.read_sql("""
SELECT productName, quantityInStock
  FROM products
 ORDER BY quantityInStock;
""", conn).head(10))
print("\n")

# Cast quantityInStock to an integer for proper ordering (first 10 rows)
print(pd.read_sql("""
SELECT productName, quantityInStock
  FROM products
 ORDER BY CAST(quantityInStock AS INTEGER);
""", conn).head(10))
print("\n")

# Same as above, but all rows
print(pd.read_sql("""
SELECT productName, quantityInStock
  FROM products
 ORDER BY CAST(quantityInStock AS INTEGER);
""", conn))
print("\n")

# Limiting results to first 5 rows from orders table
print(pd.read_sql("""
SELECT *
  FROM orders
 LIMIT 5;
""", conn))
print("\n")

# Top 10 longest comments from orders table
print(pd.read_sql("""
SELECT *
  FROM orders
 ORDER BY length(comments) DESC
 LIMIT 10;
""", conn))
print("\n")

# Top 10 longest comments from cancelled orders
print(pd.read_sql("""
SELECT *
  FROM orders
 WHERE status = "Cancelled"
 ORDER BY length(comments) DESC
 LIMIT 10;
""", conn))
print("\n")

# Top 10 longest comments from cancelled or resolved orders
print(pd.read_sql("""
SELECT *
  FROM orders
 WHERE status IN ("Cancelled", "Resolved")
 ORDER BY length(comments) DESC
 LIMIT 10;
""", conn))
print("\n")

# Distinct customer numbers and order dates, ordered by order date, limited to 5 rows
print(pd.read_sql("""
SELECT DISTINCT customerNumber, orderDate
  FROM orders
 ORDER BY orderDate
 LIMIT 5;
""", conn))
print("\n")

# Top 10 orders that have not been shipped and are not cancelled, ordered by order date descending
print(pd.read_sql("""
SELECT *
  FROM orders
 WHERE shippedDate = ""
   AND status != "Cancelled"
 ORDER BY orderDate DESC
 LIMIT 10;
""", conn))
print("\n")

# Order that took the longest time to fulfill (shippedDate - orderDate)
print(pd.read_sql("""
SELECT *,
       julianday(shippedDate) - julianday(orderDate) AS days_to_fulfill
  FROM orders
 WHERE shippedDate != ""
 ORDER BY days_to_fulfill DESC
 LIMIT 1;
""", conn))
print("\n")

conn.close()