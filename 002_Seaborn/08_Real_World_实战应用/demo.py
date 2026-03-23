#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Seaborn实战应用
展示Seaborn在实际数据分析中的应用
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置默认样式
sns.set_style("whitegrid")
sns.set_palette("deep")

# 1. 销售数据分析
def sales_analysis():
    """销售数据分析"""
    print("\n=== 销售数据分析 ===")
    
    # 创建模拟销售数据
    np.random.seed(42)
    dates = pd.date_range("2024-01-01", periods=30)
    products = ["Product A", "Product B", "Product C"]
    
    sales_data = []
    for date in dates:
        for product in products:
            sales = np.random.randint(100, 1000)
            sales_data.append({"date": date, "product": product, "sales": sales})
    
    sales_df = pd.DataFrame(sales_data)
    
    # 销售趋势图
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="date", y="sales", hue="product", data=sales_df)
    plt.title("Sales Trend by Product")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("sales_trend.png")
    plt.close()
    
    # 产品销售对比
    plt.figure(figsize=(8, 6))
    sns.barplot(x="product", y="sales", data=sales_df, estimator=np.mean)
    plt.title("Average Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Average Sales")
    plt.savefig("sales_by_product.png")
    plt.close()
    
    print("销售数据分析完成")

# 2. 客户数据分析
def customer_analysis():
    """客户数据分析"""
    print("\n=== 客户数据分析 ===")
    
    # 创建模拟客户数据
    np.random.seed(42)
    ages = np.random.randint(18, 70, 1000)
    genders = np.random.choice(["Male", "Female"], 1000)
    spending = np.random.normal(500, 100, 1000)
    spending = np.maximum(0, spending)
    
    customer_df = pd.DataFrame({"age": ages, "gender": genders, "spending": spending})
    
    # 客户年龄分布
    plt.figure(figsize=(8, 6))
    sns.histplot(customer_df["age"], bins=20, kde=True)
    plt.title("Customer Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.savefig("customer_age_dist.png")
    plt.close()
    
    # 性别与消费关系
    plt.figure(figsize=(8, 6))
    sns.boxplot(x="gender", y="spending", data=customer_df)
    plt.title("Spending by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Spending")
    plt.savefig("spending_by_gender.png")
    plt.close()
    
    # 年龄与消费关系
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="age", y="spending", data=customer_df, hue="gender")
    plt.title("Age vs Spending")
    plt.xlabel("Age")
    plt.ylabel("Spending")
    plt.savefig("age_vs_spending.png")
    plt.close()
    
    print("客户数据分析完成")

# 3. 股票数据分析
def stock_analysis():
    """股票数据分析"""
    print("\n=== 股票数据分析 ===")
    
    # 创建模拟股票数据
    np.random.seed(42)
    dates = pd.date_range("2024-01-01", periods=100)
    
    # 模拟三只股票的价格
    stock1 = 100 + np.cumsum(np.random.normal(0, 1, 100))
    stock2 = 150 + np.cumsum(np.random.normal(0, 1.5, 100))
    stock3 = 200 + np.cumsum(np.random.normal(0, 0.8, 100))
    
    stock_df = pd.DataFrame({
        "date": dates,
        "Stock A": stock1,
        "Stock B": stock2,
        "Stock C": stock3
    })
    
    # 股票价格趋势
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=stock_df.drop("date", axis=1))
    plt.title("Stock Price Trends")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("stock_trends.png")
    plt.close()
    
    # 股票相关性热力图
    stock_corr = stock_df.drop("date", axis=1).corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(stock_corr, annot=True, cmap="coolwarm")
    plt.title("Stock Price Correlations")
    plt.savefig("stock_correlation.png")
    plt.close()
    
    print("股票数据分析完成")

# 4. 天气数据分析
def weather_analysis():
    """天气数据分析"""
    print("\n=== 天气数据分析 ===")
    
    # 创建模拟天气数据
    np.random.seed(42)
    dates = pd.date_range("2024-01-01", periods=365)
    temperatures = 10 + 20 * np.sin(np.arange(365) * 2 * np.pi / 365) + np.random.normal(0, 3, 365)
    humidity = 60 + 20 * np.sin(np.arange(365) * 2 * np.pi / 365 + np.pi/2) + np.random.normal(0, 5, 365)
    humidity = np.clip(humidity, 0, 100)
    
    weather_df = pd.DataFrame({"date": dates, "temperature": temperatures, "humidity": humidity})
    weather_df["month"] = weather_df["date"].dt.month
    
    # 温度和湿度趋势
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="date", y="temperature", data=weather_df, label="Temperature")
    sns.lineplot(x="date", y="humidity", data=weather_df, label="Humidity")
    plt.title("Temperature and Humidity Trends")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("weather_trends.png")
    plt.close()
    
    # 月度平均温度
    plt.figure(figsize=(8, 6))
    sns.barplot(x="month", y="temperature", data=weather_df, estimator=np.mean)
    plt.title("Monthly Average Temperature")
    plt.xlabel("Month")
    plt.ylabel("Average Temperature")
    plt.savefig("monthly_temperature.png")
    plt.close()
    
    # 温度和湿度关系
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="temperature", y="humidity", data=weather_df)
    plt.title("Temperature vs Humidity")
    plt.xlabel("Temperature")
    plt.ylabel("Humidity")
    plt.savefig("temp_vs_humidity.png")
    plt.close()
    
    print("天气数据分析完成")

# 5. 学生成绩分析
def student_analysis():
    """学生成绩分析"""
    print("\n=== 学生成绩分析 ===")
    
    # 创建模拟学生成绩数据
    np.random.seed(42)
    subjects = ["Math", "English", "Science", "History"]
    grades = []
    
    for subject in subjects:
        for i in range(100):
            grade = np.random.normal(70, 15, 1)[0]
            grade = np.clip(grade, 0, 100)
            grades.append({"subject": subject, "grade": grade})
    
    student_df = pd.DataFrame(grades)
    
    # 科目成绩分布
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="subject", y="grade", data=student_df)
    plt.title("Grade Distribution by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Grade")
    plt.savefig("grade_distribution.png")
    plt.close()
    
    # 科目成绩小提琴图
    plt.figure(figsize=(10, 6))
    sns.violinplot(x="subject", y="grade", data=student_df)
    plt.title("Grade Distribution by Subject (Violin Plot)")
    plt.xlabel("Subject")
    plt.ylabel("Grade")
    plt.savefig("grade_violin.png")
    plt.close()
    
    # 成绩分布直方图
    plt.figure(figsize=(8, 6))
    sns.histplot(student_df["grade"], bins=20, kde=True)
    plt.title("Overall Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Count")
    plt.savefig("overall_grade_dist.png")
    plt.close()
    
    print("学生成绩分析完成")

# 主函数
def main():
    print("Seaborn Real World Applications")
    print("=" * 50)
    
    # 运行所有示例
    sales_analysis()
    customer_analysis()
    stock_analysis()
    weather_analysis()
    student_analysis()
    
    print("\nAll real world applications completed!")

if __name__ == "__main__":
    main()