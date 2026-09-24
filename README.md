# 📱 Mobile Sales Data Analysis using Python

A Python-based data analysis and visualization project that analyzes mobile phone sales data using **Pandas, Matplotlib, and Seaborn**.

The project explores mobile products, categories, prices, quantities sold, customer age, storage capacity, and ratings to understand sales patterns and relationships within the dataset.

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook / VS Code

## 📊 Dataset Features

The dataset contains **100 mobile sales records** with the following columns:

| Column       | Description                   |
| ------------ | ----------------------------- |
| Product      | Mobile phone brand/model      |
| Category     | Premium, Mid-Range, or Budget |
| Price        | Mobile phone price            |
| Quantity     | Number of units sold          |
| Storage      | Storage capacity              |
| Customer_Age | Age of the customer           |
| Rating       | Customer rating               |

## 🔍 Analysis Performed

### Data Exploration

* Display complete dataset
* View first 5 and first 3 rows
* View last 5 and last 3 rows
* Find number of rows and columns
* Check data types
* Display dataset information

### Statistical Analysis

* Average mobile price
* Average customer rating
* Lowest mobile price
* Highest mobile price
* Total quantity sold
* Average price by category
* Total quantity sold by category

### 📈 Data Visualizations

The project creates the following visualizations:

1. **Bar Chart** – Quantity Sold by Mobile Category
2. **Histogram** – Distribution of Mobile Prices
3. **Box Plot** – Price Distribution and Outliers by Category
4. **Scatter Plot** – Mobile Price vs Rating
5. **Correlation Heatmap** – Relationship between numerical variables

## 📌 Key Python Concepts

This project demonstrates the use of:

```python
pd.DataFrame()
df.head()
df.tail()
df.shape
df.dtypes
df.info()
df.mean()
df.min()
df.max()
df.sum()
df.groupby()
df.corr()
```

It also demonstrates visualization techniques using:

```python
sns.barplot()
plt.hist()
sns.boxplot()
sns.scatterplot()
sns.heatmap()
```

## 📂 Project Structure

```text
Mobile-Sales-Data-Analysis/
│
├── mobile_sales_analysis.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Install required libraries

```bash
pip install pandas matplotlib seaborn
```

### 3. Run the Python program

```bash
python mobile_sales_analysis.py
```

The program will display the data analysis results and generate multiple visualizations.

## 🎯 Project Objective

The main objective of this project is to practice **data analysis and visualization using Python** and understand how sales data can be explored using statistical operations and graphical representations.

## 👨‍💻 Author

**Kirubakaran K**

CSE Student | Python | Data Analysis | Web Development

---

⭐ If you find this project useful, feel free to star the repository.
