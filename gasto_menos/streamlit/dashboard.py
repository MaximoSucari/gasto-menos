import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt


def fetch_data(phone_number):
    api_endpoint = "http://127.0.0.1:8000/expenses/list/"
    payload = {"from": phone_number}

    try:
        response = requests.get(api_endpoint, json=payload)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return None


def main():
    st.title("Gastos por Categoría")

    phone_number = "1126603201"
    if phone_number:
        result = fetch_data(phone_number)
        data = result.get("response", {})

        # Make two containers side-by-side
        left_column, right_column = st.columns(2)

        with left_column:
            df = pd.DataFrame(data)
            df = df[["amount", "currency", "message", "category__name", "date"]]
            st.data_editor(df, num_rows="dynamic")

        with right_column:
            fig, ax = plt.subplots()
            df["category__name"].value_counts().plot(ax=ax, kind="pie")
            plt.title("Expenses by Category")
            plt.ylabel("")
            st.pyplot(fig)


if __name__ == "__main__":
    main()
