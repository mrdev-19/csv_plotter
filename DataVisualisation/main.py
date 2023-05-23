import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Disable warning about pyplot global use
st.set_option('deprecation.showPyplotGlobalUse', False)

# Set page title
st.title("CSV File Plotter")
hide_ele="""
        <style>
        #Mainmenu {visibility:hidden;}
        footer {visibility:hidden;}
        header {visibility:hidden;}
        </style>
        """
st.markdown(hide_ele,unsafe_allow_html=True)
# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV data into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame
    st.subheader("Data Preview")
    st.write(df)

    # Plot options
    plot_options = st.multiselect("Select columns to plot", df.columns)

    if plot_options:
        plot_type = st.selectbox("Select plot type", ["Line Plot", "Scatter Plot", "Histogram"])

        # Plot based on selected options
        if plot_type == "Line Plot":
            fig, ax = plt.subplots()
            for column in plot_options:
                ax.plot(df[column], label=column)
            ax.set_xlabel("Index")
            ax.set_ylabel("Values")
            ax.set_title("Line Plot")
            ax.legend()
            st.pyplot(fig)

        elif plot_type == "Scatter Plot":
            fig, ax = plt.subplots()
            for column in plot_options:
                ax.scatter(df.index, df[column], label=column)
            ax.set_xlabel("Index")
            ax.set_ylabel("Values")
            ax.set_title("Scatter Plot")
            ax.legend()
            st.pyplot(fig)

        elif plot_type == "Histogram":
            fig, ax = plt.subplots()
            for column in plot_options:
                sns.histplot(df[column], kde=True, label=column)
            ax.set_xlabel("Values")
            ax.set_ylabel("Frequency")
            ax.set_title("Histogram")
            ax.legend()
            st.pyplot(fig)
