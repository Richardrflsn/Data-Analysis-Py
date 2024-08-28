import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='darkgrid')

# Load data
df = pd.read_csv("combined_data.csv")

df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# Sidebar 
st.sidebar.title("Menu")
menu = st.sidebar.radio("Select Menu", ["Dashboard", "Purchase Frequency Distribution", "Payment Method Trends"])

if menu == "Dashboard":
    st.header("E-Commerce Data Analysis 💼")
    
    # Group by city
    city_distribution = df.groupby('customer_city')['order_id'].nunique().reset_index()
    city_distribution = city_distribution.sort_values(by='order_id', ascending=False).head(10)
    
    # Group by state
    state_distribution = df.groupby('customer_state')['order_id'].nunique().reset_index()
    state_distribution = state_distribution.sort_values(by='order_id', ascending=False).head(10)
    
    # Plot by city
    st.subheader("Top 10 Cities by Purchase Frequency")
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.barplot(x='order_id', y='customer_city', data=city_distribution, palette='Blues_d', ax=ax)
    ax.set_xlabel("Number of Orders")
    ax.set_ylabel("City")
    ax.set_title("Top 10 Cities by Purchase Frequency")
    st.pyplot(fig)
    
    # Plot by state
    st.subheader("Top 10 States by Purchase Frequency")
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.barplot(x='order_id', y='customer_state', data=state_distribution, palette='Greens_d', ax=ax)
    ax.set_xlabel("Number of Orders")
    ax.set_ylabel("State")
    ax.set_title("Top 10 States by Purchase Frequency")
    st.pyplot(fig)
    
    # Payment Method Trends
    st.subheader("Most Frequently Used Payment Methods Over Time")
    
    # Group by payment type and order date 
    payment_trends = df.set_index('order_purchase_timestamp').groupby([pd.Grouper(freq='M'), 'payment_type'])['order_id'].nunique().reset_index()
    
    # Plot payment method trends
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.lineplot(x='order_purchase_timestamp', y='order_id', hue='payment_type', data=payment_trends, marker='o', ax=ax)
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Orders")
    ax.set_title("Payment Method Trends Over Time")
    ax.legend(title='Payment Type')
    st.pyplot(fig)

    st.subheader("Payment Method Distribution")

    payment_method_distribution = df['payment_type'].value_counts()
    payment_method_percentages = (payment_method_distribution / payment_method_distribution.sum()) * 100

    # Create a pie chart
    fig, ax = plt.subplots(figsize=(14, 6))
    colors = plt.cm.Paired(range(len(payment_method_percentages)))

    ax.pie(
        payment_method_percentages, 
        labels=payment_method_percentages.index, 
        autopct='%1.3f%%', 
        colors=colors,
        startangle=140
    )

    ax.set_title('Distribusi Metode Pembayaran (Pie Chart)')

    # Show the plot
    st.pyplot(fig)

elif menu == "Purchase Frequency Distribution":
    st.header("Purchase Frequency Distribution by Region")

    # Group by city
    city_distribution = df.groupby('customer_city')['order_id'].nunique().reset_index()
    city_distribution = city_distribution.sort_values(by='order_id', ascending=False).head(10)
    
    # Group by state
    state_distribution = df.groupby('customer_state')['order_id'].nunique().reset_index()
    state_distribution = state_distribution.sort_values(by='order_id', ascending=False).head(10)
    
    # Plot by city
    st.subheader("Top 10 Cities by Purchase Frequency")
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.barplot(x='order_id', y='customer_city', data=city_distribution, palette='Blues_d', ax=ax)
    ax.set_xlabel("Number of Orders")
    ax.set_ylabel("City")
    ax.set_title("Top 10 Cities by Purchase Frequency")
    st.pyplot(fig)
    
    # Plot by state
    st.subheader("Top 10 States by Purchase Frequency")
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.barplot(x='order_id', y='customer_state', data=state_distribution, palette='Greens_d', ax=ax)
    ax.set_xlabel("Number of Orders")
    ax.set_ylabel("State")
    ax.set_title("Top 10 States by Purchase Frequency")
    st.pyplot(fig)

elif menu == "Payment Method Trends":
    st.header("Most Frequently Used Payment Methods Over Time")
    payment_method_distribution = df['payment_type'].value_counts()

    # Create DataFrame for the table
    payment_method_df = payment_method_distribution.reset_index()
    payment_method_df.columns = ['Payment Method', 'Count']

    # Calculate percentage
    payment_method_df['Percentage'] = (payment_method_df['Count'] / payment_method_df['Count'].sum()) * 100

    # Format percentage to three decimal places
    payment_method_df['Percentage'] = payment_method_df['Percentage'].map('{:.3f}%'.format)

    # Display the table
    st.header("Distribusi Metode Pembayaran")
    st.table(payment_method_df)

    # Group by payment type and order date
    payment_trends = df.set_index('order_purchase_timestamp').groupby([pd.Grouper(freq='M'), 'payment_type'])['order_id'].nunique().reset_index()
    
    # Plot payment method trends
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.lineplot(x='order_purchase_timestamp', y='order_id', hue='payment_type', data=payment_trends, marker='o', ax=ax)
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Orders")
    ax.set_title("Payment Method Trends Over Time")
    ax.legend(title='Payment Type')
    st.pyplot(fig)

    payment_method_distribution = df['payment_type'].value_counts()
    payment_method_percentages = (payment_method_distribution / payment_method_distribution.sum()) * 100

    st.header("Payment Method Distribution")

    # Create a pie chart
    fig, ax = plt.subplots(figsize=(14, 6))
    colors = plt.cm.Paired(range(len(payment_method_percentages)))

    ax.pie(
        payment_method_percentages, 
        labels=payment_method_percentages.index, 
        autopct='%1.3f%%', 
        colors=colors,
        startangle=140
    )

    ax.set_title('Distribusi Metode Pembayaran (Pie Chart)')

    # Show the plot
    st.pyplot(fig)
