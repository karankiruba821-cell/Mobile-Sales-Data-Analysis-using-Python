import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data={
    "Product":[
        "iPhone","Samsung Galaxy","OnePlus","Redmi","Vivo","Oppo","Realme","Google Pixel","Nothing Phone","Motorola",
        "iPhone","Samsung Galaxy","OnePlus","Redmi","Vivo","Oppo","Realme","Google Pixel","Nothing Phone","Motorola",
        "iPhone","Samsung Galaxy","OnePlus","Redmi","Vivo","Oppo","Realme","Google Pixel","Nothing Phone","Motorola",
        "iPhone","Samsung Galaxy","OnePlus","Redmi","Vivo","Oppo","Realme","Google Pixel","Nothing Phone","Motorola",
        "iPhone","Samsung Galaxy","OnePlus","Redmi","Vivo","Oppo","Realme","Google Pixel","Nothing Phone","Motorola",
        "iPhone","Samsung Galaxy","OnePlus","Redmi","Vivo","Oppo","Realme","Google Pixel","Nothing Phone","Motorola",
        "iPhone","Samsung Galaxy","OnePlus","Redmi","Vivo","Oppo","Realme","Google Pixel","Nothing Phone","Motorola",
        "iPhone","Samsung Galaxy","OnePlus","Redmi","Vivo","Oppo","Realme","Google Pixel","Nothing Phone","Motorola",
        "iPhone","Samsung Galaxy","OnePlus","Redmi","Vivo","Oppo","Realme","Google Pixel","Nothing Phone","Motorola",
        "iPhone","Samsung Galaxy","OnePlus","Redmi","Vivo","Oppo","Realme","Google Pixel","Nothing Phone","Motorola"
    ],

    "Category":[
        "Premium","Premium","Mid-Range","Budget","Mid-Range","Mid-Range","Budget","Premium","Mid-Range","Budget",
        "Premium","Premium","Mid-Range","Budget","Mid-Range","Mid-Range","Budget","Premium","Mid-Range","Budget",
        "Premium","Premium","Mid-Range","Budget","Mid-Range","Mid-Range","Budget","Premium","Mid-Range","Budget",
        "Premium","Premium","Mid-Range","Budget","Mid-Range","Mid-Range","Budget","Premium","Mid-Range","Budget",
        "Premium","Premium","Mid-Range","Budget","Mid-Range","Mid-Range","Budget","Premium","Mid-Range","Budget",
        "Premium","Premium","Mid-Range","Budget","Mid-Range","Mid-Range","Budget","Premium","Mid-Range","Budget",
        "Premium","Premium","Mid-Range","Budget","Mid-Range","Mid-Range","Budget","Premium","Mid-Range","Budget",
        "Premium","Premium","Mid-Range","Budget","Mid-Range","Mid-Range","Budget","Premium","Mid-Range","Budget",
        "Premium","Premium","Mid-Range","Budget","Mid-Range","Mid-Range","Budget","Premium","Mid-Range","Budget",
        "Premium","Premium","Mid-Range","Budget","Mid-Range","Mid-Range","Budget","Premium","Mid-Range","Budget"
    ],

    "Price":[
        79999,69999,39999,14999,29999,27999,14999,69999,32999,17999,
        84999,72999,42999,15999,31999,28999,15999,74999,34999,18999,
        74999,64999,37999,13999,28999,25999,13999,67999,29999,16999,
        89999,79999,44999,17999,32999,29999,16999,79999,36999,19999,
        79999,69999,39999,14999,30999,27999,14999,72999,32999,17999,
        82999,71999,41999,15999,29999,28999,15999,74999,34999,18999,
        77999,67999,40999,14999,31999,26999,14999,69999,33999,17999,
        86999,75999,43999,16999,32999,29999,16999,77999,35999,19999,
        73999,65999,38999,13999,28999,25999,13999,67999,31999,16999,
        91999,78999,46999,18999,33999,30999,17999,81999,37999,20999
    ],

    "Quantity":[
        3,4,6,8,5,4,9,3,5,7,
        2,5,7,10,6,5,11,4,6,8,
        4,3,8,9,5,6,12,3,7,9,
        2,4,6,11,7,5,10,4,6,8,
        3,5,7,9,6,4,13,3,5,10,
        4,4,8,12,5,6,11,4,7,9,
        3,6,7,10,8,5,12,3,6,11,
        2,5,9,13,6,7,10,4,8,9,
        4,3,8,11,7,5,13,3,6,10,
        3,5,10,12,6,8,11,4,7,9
    ],

    "Storage":[
        "256GB","256GB","128GB","128GB","128GB","256GB","128GB","256GB","256GB","128GB",
        "512GB","256GB","256GB","128GB","256GB","128GB","128GB","512GB","256GB","128GB",
        "256GB","128GB","256GB","128GB","128GB","256GB","128GB","256GB","256GB","128GB",
        "512GB","256GB","256GB","128GB","256GB","128GB","128GB","512GB","256GB","128GB",
        "256GB","256GB","128GB","128GB","256GB","256GB","128GB","256GB","256GB","128GB",
        "512GB","256GB","256GB","128GB","128GB","256GB","128GB","512GB","256GB","128GB",
        "256GB","128GB","256GB","128GB","256GB","128GB","128GB","256GB","256GB","128GB",
        "512GB","256GB","128GB","128GB","256GB","256GB","128GB","512GB","256GB","128GB",
        "256GB","256GB","128GB","128GB","256GB","128GB","128GB","256GB","256GB","128GB",
        "512GB","256GB","256GB","128GB","256GB","256GB","128GB","512GB","256GB","128GB"
    ],

    "Customer_Age":[
        22,28,24,31,35,42,21,26,38,29,
        25,32,23,34,41,45,27,24,36,30,
        20,29,26,33,39,48,22,28,35,31,
        24,37,25,29,43,40,23,27,34,32,
        21,30,28,36,38,44,26,25,39,29,
        27,34,22,31,40,46,24,29,37,33,
        23,28,27,35,42,41,21,26,38,30,
        26,31,24,32,37,43,25,28,36,34,
        22,35,29,30,41,47,23,27,39,31,
        25,33,21,36,44,45,24,29,40,32
    ],

    "Rating":[
        4.2,4.5,4.3,4.6,4.1,4.7,4.0,4.3,4.6,4.4,
        4.1,4.4,4.2,4.5,4.0,4.6,4.3,4.1,4.7,4.5,
        4.4,4.2,4.5,4.3,4.1,4.8,4.2,4.4,4.6,4.3,
        4.5,4.3,4.1,4.6,4.2,4.7,4.4,4.2,4.8,4.5,
        4.3,4.6,4.4,4.2,4.0,4.7,4.1,4.5,4.6,4.4,
        4.2,4.4,4.3,4.5,4.1,4.8,4.3,4.2,4.7,4.5,
        4.6,4.3,4.2,4.7,4.4,4.6,4.1,4.5,4.8,4.3,
        4.1,4.5,4.4,4.6,4.2,4.7,4.3,4.1,4.6,4.4,
        4.3,4.6,4.1,4.5,4.4,4.7,4.2,4.3,4.6,4.5,
        4.5,4.2,4.4,4.7,4.1,4.8,4.3,4.5,4.7,4.2
    ]
}

df=pd.DataFrame(data)

print("MOBILE SALES DATA")
print(df)

print("\nFIRST 5 ROWS")
print(df.head())

print("\nFIRST 3 ROWS")
print(df.head(3))

print("\nLAST 5 ROWS")
print(df.tail())

print("\nLAST 3 ROWS")
print(df.tail(3))

print("\nNUMBER OF ROWS AND COLUMNS")
print(df.shape)

print("\nNUMBER OF ROWS:",df.shape[0])
print("NUMBER OF COLUMNS:",df.shape[1])

print("\nDATA TYPES")
print(df.dtypes)

print("\nDATA INFORMATION")
df.info()

print("\nAVERAGE PRICE")
print(df["Price"].mean())

print("\nAVERAGE RATING")
print(df["Rating"].mean())

print("\nLOWEST PRICE")
print(df["Price"].min())

print("\nHIGHEST PRICE")
print(df["Price"].max())

print("\nTOTAL QUANTITY SOLD")
print(df["Quantity"].sum())

print("\nAVERAGE PRICE BY CATEGORY")
print(df.groupby("Category")["Price"].mean())

print("\nTOTAL QUANTITY BY CATEGORY")
print(df.groupby("Category")["Quantity"].sum())

plt.figure(figsize=(8,5))
sns.barplot(data=df,x="Category",y="Quantity")
plt.title("Quantity Sold by Mobile Category")
plt.xlabel("Category")
plt.ylabel("Quantity")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["Price"],bins=8)
plt.xlabel("Price")
plt.ylabel("Number of Mobiles")
plt.title("Distribution of Mobile Prices")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(data=df,x="Category",y="Price")
plt.xlabel("Category")
plt.ylabel("Price")
plt.title("Price Distribution and Outliers by Category")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(data=df,x="Price",y="Rating")
plt.xlabel("Price")
plt.ylabel("Rating")
plt.title("Mobile Price vs Rating")
plt.show()

correlation=df[["Price","Quantity","Customer_Age","Rating"]].corr()

print("\nCORRELATION MATRIX")
print(correlation)

plt.figure(figsize=(8,5))
sns.heatmap(correlation,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Mobile Sales Correlation Heatmap")
plt.show()