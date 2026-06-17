# ☕ Coffee Shop Sales Analysis Dashboard

##  Project Overview

This project analyzes a coffee shop sales dataset containing **149,116 transactions**. The objective was to transform raw sales data into actionable business insights using a complete analytics workflow:

**Python → MySQL → Power BI**

The project focuses on identifying sales trends, customer purchasing behavior, product performance, and revenue drivers to support business decision-making.

---

##  Tools Used

- Python (Pandas)
- MySQL
- Power BI
- GitHub

---

##  Dataset Information

The dataset contains the following fields:

- Transaction ID
- Transaction Date
- Transaction Time
- Quantity Sold
- Store Location
- Product Category
- Product Type
- Product Details
- Unit Price

**Total Records:** 149,116

---

##  Project Workflow

### 1. Data Cleaning (Python)

- Removed unnecessary columns
- Checked and handled missing values
- Converted data types
- Standardized date formats
- Exported cleaned dataset for SQL analysis

### 2. Data Analysis (MySQL)

Performed business-focused analysis including:

- Revenue by product category
- Revenue by store location
- Monthly revenue trends
- Revenue by weekday
- Revenue by time of day
- Top-selling products
- Transaction analysis

### 3. Dashboard Development (Power BI)

Created an interactive dashboard featuring:

#### KPI Cards

- Total Revenue
- Total Transactions
- Average Order Value
- Top Selling Product

#### Visualizations

- Monthly Revenue Trend
- Revenue by Product Category
- Revenue by Store Location
- Revenue by Weekday
- Revenue by Time Period
- Top Products Analysis
- Interactive Slicers and Filters

---

#  Key Findings

## Revenue by Time of Day

| Time Period | Transactions | Revenue |
|------------|-------------:|---------:|
| Morning | 81,751 | ₹388,288.67 |
| Afternoon | 44,427 | ₹204,720.83 |
| Evening | 22,938 | ₹105,802.83 |

### Insights

- Morning sales generate approximately **56% of total revenue**.
- Customer activity is heavily concentrated during morning hours.
- Revenue declines significantly after noon.

---

## Revenue by Product Category

| Category | Revenue |
|----------|---------:|
| Coffee | ₹269,952.45 |
| Tea | ₹196,405.95 |
| Bakery | ₹82,315.64 |
| Drinking Chocolate | ₹72,416.00 |
| Coffee Beans | ₹40,085.25 |
| Branded | ₹13,607.00 |
| Loose Tea | ₹11,213.60 |
| Flavours | ₹8,408.80 |
| Packaged Chocolate | ₹4,407.64 |

### Insights

- Coffee is the highest revenue-generating category, contributing approximately **39% of total revenue**.
- Tea contributes approximately **28% of total revenue**.
- Coffee and Tea together account for nearly **67% of total revenue**.
- Bakery is the strongest-performing non-beverage category.
- Specialty categories contribute only a small portion of overall sales.

---

## Revenue by Weekday

| Day | Revenue |
|------|---------:|
| Monday | ₹101,677 |
| Tuesday | ₹99,456 |
| Wednesday | ₹100,314 |
| Thursday | ₹100,768 |
| Friday | ₹101,373 |
| Saturday | ₹96,894 |
| Sunday | ₹98,330 |

### Insights

- Revenue remains consistent throughout the week.
- No single day dominates overall sales.
- Weekend sales are slightly lower than weekday sales.
- The business demonstrates stable customer demand.

---

#  Business Recommendations

## 1. Prioritize Morning Operations

Since approximately **56% of revenue is generated during morning hours**:

- Schedule additional staff during peak periods.
- Maintain sufficient inventory during morning hours.
- Focus on reducing service wait times.

---

## 2. Focus Marketing on Core Revenue Drivers

Coffee and Tea contribute approximately **67% of total revenue**.

Recommended actions:

- Promote coffee and tea products.
- Introduce seasonal beverage offerings.
- Ensure strong inventory management of top-selling drinks.

---

## 3. Increase Afternoon and Evening Traffic

Revenue drops significantly after morning hours.

Potential strategies:

- Afternoon discounts
- Happy hour promotions
- Evening combo offers
- Loyalty rewards programs

---

## 4. Leverage Bakery Cross-Selling Opportunities

Bakery products generate significant revenue and naturally complement beverages.

Recommended actions:

- Coffee + Bakery combo deals
- Breakfast bundles
- Upselling bakery products during beverage purchases

---

## 5. Review Low-Performing Categories

Low-performing categories include:

- Packaged Chocolate
- Flavours
- Loose Tea

Potential actions:

- Pricing review
- Promotional campaigns
- Product assortment optimization
- Shelf-space reallocation

---

#  Skills Demonstrated

- Data Cleaning using Python (Pandas)
- SQL Querying and Analysis
- Data Modeling
- Power BI Dashboard Development
- DAX Measures
- KPI Design
- Data Visualization
- Business Intelligence Reporting
- Data Storytelling

---


#  Project Outcome

This project demonstrates an end-to-end data analytics workflow, transforming raw transaction data into actionable business insights and recommendations that can support operational, marketing, and inventory decisions for a coffee shop business.
