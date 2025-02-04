# 💎 Gemineye Jewelry Price Optimization

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

A data-driven solution for optimizing pricing strategies in luxury jewelry retail.

## 📖 Overview
**Gemineye** is a luxury jewelry retailer facing challenges with pricing strategies. This project develops machine learning models to:
- Predict optimal jewelry prices
- Implement dynamic pricing strategies
- Maximize revenue and profit margins

![Sales Comparison](https://via.placeholder.com/600x300?text=Sales+Trend+Visualization)

## 🗂️ Dataset Overview
| Feature | Description | Key Insights |
|---------|-------------|--------------|
| `Price_USD` | Jewelry price (target) | Mean: $362.21, Max: $34k+ |
| `Category` | Product category | Earrings (29k) & Rings (26k) dominate |
| `Order_datetime` | Purchase timestamp | Peak sales at 10AM-12PM |
| `Main_metal` | Primary metal used | Gold/Silver most common |
| `User_ID` | Customer identifier | 3 distinct spending clusters |

[Full feature description](#dataset-details)

## 🔍 Key Insights

### 💵 Price Analysis
- **Right-skewed distribution**: 75% of items < $431, but outliers reach $34k+
- **COVID impact**: 2020-2021 sales accounted for 85.3% of total revenue
- **Premium clusters**: 3 customer segments identified (moderate, bulk, premium buyers)

### 📈 Sales Trends
- **2018-2021 Growth**: 117 → 55,255 units sold
- **Peak hours**: 10AM-2PM (optimal marketing window)
- **Category performance**: 
  - 🥇 Earrings (29,047 units)
  - 🥈 Rings (26,025 units)
  - 🥉 Pendants (13,083 units)

### 🧑🤝🧑 Customer Segmentation
| Cluster | Avg Spend | Strategy |
|---------|-----------|----------|
| 0️⃣ Moderate | $679 | Loyalty programs |
| 1️⃣ Bulk | $137k | Volume discounts |
| 2️⃣ Premium | $37k | Bundle offers |

## 🧠 Model Performance
| Model | Train R² | Test R² | RMSE |
|-------|----------|---------|------|
| Linear Regression | 0.074 | 0.106 | $370 |
| Random Forest | 0.891 | 0.885 | $98 |
| Gradient Boosting | 0.902 | 0.894 | $92 |
| Neural Network | 0.915 | 0.901 | $88 |

## 💡 Recommendations
1. **Dynamic Pricing**
   - 🏷️ Premium pricing for luxury clusters (Brands 0.0 & 5.0)
   - 🎯 Competitive pricing for mid-range categories (Pendants, Bracelets)

2. **Inventory Management**
   - 📦 Prioritize high-demand categories (Earrings & Rings)
   - 🗑️ Phase out low-performance categories (Studs, Souvenirs)

3. **Customer Engagement**
   - 💎 VIP programs for bulk buyers (Cluster 1)
   - 🎁 Bundle offers for premium buyers (Cluster 2)

## 🛠️ Installation
```bash
git clone https://github.com/yourusername/gemineye-pricing.git
cd gemineye-pricing
pip install -r requirements.txt
