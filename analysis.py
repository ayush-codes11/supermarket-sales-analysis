import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the CSV file
df = pd.read_csv('supermarket_Sales.csv')

# Print basic info
print("Shape of the dataset:", df.shape)
print("\nColumn names:\n", df.columns.tolist())

# Show the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values per column:")
print(df.isnull().sum())

# Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Check new column names
print("\nCleaned column names:")
print(df.columns.tolist())

# Check dataset info and summary statistics
print("\nDataset Info:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

# Create a new column for total sale amount
df['total'] = df['quantity'] * df['unit_price']

print("\nPreview of 'total' column:")
print(df[['quantity', 'unit_price', 'total']].head())

# Total sales per city
city_sales = df.groupby('city')['total'].sum().sort_values(ascending=False)

print("\nTotal Sales by City:")
print(city_sales)

# Bar chart of sales by city
plt.figure(figsize=(8, 5))
sns.barplot(x=city_sales.values, y=city_sales.index, palette='Blues_d')
plt.title('Total Sales by City')
plt.xlabel('Sales')
plt.ylabel('City')
plt.tight_layout()
plt.show()

# Total sales by product line
product_sales = df.groupby('product_line')['total'].sum().sort_values(ascending=False)

print("\nTotal Sales by Product Line:")
print(product_sales)

# Bar chart for product line sales
plt.figure(figsize=(8, 5))
sns.barplot(x=product_sales.values, y=product_sales.index, palette='Greens_r')
plt.title('Total Sales by Product Line')
plt.xlabel('Sales')
plt.ylabel('Product Line')
plt.tight_layout()
plt.show()

# Convert invoice_time to datetime and extract hour
df['invoice_time'] = pd.to_datetime(df['time'])
df['hour'] = df['invoice_time'].dt.hour

# Count number of transactions by hour
transactions_by_hour = df['hour'].value_counts().sort_index()

print("\nTransactions by Hour:")
print(transactions_by_hour)

# Line plot for transactions by hour
plt.figure(figsize=(8, 5))
sns.lineplot(x=transactions_by_hour.index, y=transactions_by_hour.values, marker='o')
plt.title('Number of Transactions by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Transactions')
plt.xticks(range(24))  # to show every hour
plt.tight_layout()
plt.show()

# Count of each payment type
payment_counts = df['payment'].value_counts()

print("\nPayment Method Counts:")
print(payment_counts)

# Pie chart of payment types
plt.figure(figsize=(6, 6))
plt.pie(payment_counts.values, labels=payment_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Distribution of Payment Methods')
plt.tight_layout()
plt.show()

# ------------------------------------------
# Monthly Sales Trend
# ------------------------------------------

# Convert the 'date' column to datetime (if not already)
df['invoice_date'] = pd.to_datetime(df['date'])

# Extract the month in YYYY-MM format
df['month'] = df['invoice_date'].dt.to_period('M')

# Group by month and calculate total sales
monthly_sales = df.groupby('month')['total'].sum()

# Plotting the monthly sales trend
plt.figure(figsize=(8, 5))
monthly_sales.plot(marker='o', color='coral')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------------------
# Top Product Lines by Total Revenue
# ------------------------------------------

# Total revenue by product line
top_products = df.groupby('product_line')['total'].sum().sort_values(ascending=False)

# Plot the top product lines
plt.figure(figsize=(8, 5))
sns.barplot(x=top_products.values, y=top_products.index, palette='Purples')
plt.title('Top Product Lines by Revenue')
plt.xlabel('Total Sales')
plt.ylabel('Product Line')
plt.tight_layout()
plt.show()

# ------------------------------------------
# Sales by Gender & Product Line
# ------------------------------------------

# Group by gender and product line, sum total sales
gender_product_sales = df.groupby(['gender', 'product_line'])['total'].sum().unstack()

# Plot grouped bar chart
gender_product_sales.plot(kind='bar', figsize=(10, 6))
plt.title('Total Sales by Gender and Product Line')
plt.xlabel('Gender')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.legend(title='Product Line', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()




