#Cohort Analysis and Customer Segmentation Using K-Means  

This repository contains an implementation of a Cohort Analysis and Customer Segmentation project for an e-commerce business. The project focuses on analyzing customer behavior, retention patterns, and segmentation using clustering techniques to provide actionable insights for enhancing customer engagement.  

---

## Table of Contents  
1. [Project Overview](#project-overview)  
2. [Objectives](#objectives)  
3. [Dataset Description](#dataset-description)  
4. [Analysis Steps](#analysis-steps)  
5. [Key Insights](#key-insights)  
6. [Technologies Used](#technologies-used)  
7. [How to Use](#how-to-use)  
8. [Results](#results)  
9. [Future Work](#future-work)  
10. [Contributors](#contributors)  

---

## Project Overview  

E-commerce businesses often face challenges in retaining customers and improving the shopping experience. This project leverages Cohort Analysis and K-Means Clustering to:  

- Analyze customer retention rates over time.  
- Identify purchasing behaviors and trends.  
- Segment customers into meaningful groups to enable targeted marketing strategies.  

The analysis incorporates the RFM (Recency, Frequency, Monetary) framework and uses Python for implementation.  

---

## Objectives  

The primary objectives of this project are:  
1. Perform a cohort analysis to understand customer retention over time.  
2. Segment customers into groups using K-Means clustering based on their purchasing behavior.  
3. Provide actionable insights to improve retention and customer loyalty.  

---

## Dataset Description  

The dataset used in this project contains the following columns:  

| Column       | Description                                           |  
|--------------|-------------------------------------------------------|  
| InvoiceNo    | Unique identifier for each invoice or transaction.    |  
| InvoiceDate  | Date and time of the transaction.                     |  
| CustomerID   | Unique identifier for each customer.                  |  
| StockCode    | Code for specific products in the inventory.          |  
| Description  | Description of the purchased product.                 |  
| Quantity     | Number of units purchased in the transaction.         |  
| UnitPrice    | Price per unit of the product.                        |  
| Country      | Country where the transaction took place.             |  

---

## Analysis Steps  

### 1. Data Preprocessing  
- Handle missing values.  
- Clean and transform the data for analysis.  
- Extract cohort dates and calculate cohort indices.  

### 2. Cohort Analysis  
- Group customers by their first purchase date (cohort date).  
- Analyze retention rates over time.  

### 3. Feature Engineering  
- Create aggregated features such as recency, total quantity, and average order value for each customer.  

### 4. Clustering  
- Use the K-Means clustering algorithm to group customers based on purchasing behavior.  
- Apply the Elbow Method to determine the optimal number of clusters.  

### 5. Insights Extraction  
- Analyze the top products and regions for each cluster.  
- Generate actionable recommendations based on clustering results.  

---

## Key Insights  

Customers were segmented into three distinct clusters based on their purchasing patterns:  

- **Cluster 0**: Customers with moderate purchases and less frequent activity.  
- **Cluster 1**: Highly engaged customers with frequent and high-value purchases.  
- **Cluster 2**: Recently active customers with lower purchase volumes.  

The analysis identified top-performing products and regions within each cluster, enabling more focused and personalized marketing strategies.  

---

## Technologies Used  

- **Programming Language**: Python  
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
- **Tools**: Jupyter Notebook, Google Colab, Git  

---

## How to Use  

1. Clone this repository:  

```bash  
git clone 
