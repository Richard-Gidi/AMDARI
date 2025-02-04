{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPdDIiugHnRy7H3o8tYME9u",
      "include_colab_link": False
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Richard-Gidi/AMDARI/blob/main/PRICE_OPTIMIZATION/stream.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#!pip install streamlit"
      ],
      "metadata": {
        "id": "i81886yQRjfO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import joblib\n",
        "import pandas as pd"
      ],
      "metadata": {
        "id": "h64L1xd_MND1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Load the trained model\n",
        "model = joblib.load('models/jewelry_price_optimizer_linear.pkl')"
      ],
      "metadata": {
        "id": "oXkrSoM3MQeY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "IvSCRHTlMIVG"
      },
      "outputs": [],
      "source": [
        "\n",
        "# Define model metrics (replace with your actual metrics)\n",
        "METRICS = {\n",
        "    \"Train R²\": 0.85,  # Replace with your values\n",
        "    \"Test R²\": 0.80,\n",
        "    \"Train RMSE\": 10.5,\n",
        "    \"Test RMSE\": 12.3,\n",
        "    \"Generalization Error\": 1.8\n",
        "}\n",
        "\n",
        "def user_input_features():\n",
        "    st.sidebar.header(\"Model Performance Metrics\")\n",
        "    for metric, value in METRICS.items():\n",
        "        st.sidebar.text(f\"{metric}: {value:.2f}\")\n",
        "\n",
        "    st.header(\"Input Features\")\n",
        "\n",
        "    # Numerical inputs\n",
        "    year = st.number_input(\"Year\", min_value=2018, max_value=2023, value=2020)\n",
        "    month = st.number_input(\"Month\", min_value=1, max_value=12, value=1)\n",
        "    hour = st.number_input(\"Hour\", min_value=0, max_value=23, value=12)\n",
        "\n",
        "    # Main metal selection\n",
        "    main_metal = st.selectbox(\"Main Metal\", [\"None\", \"platinum\", \"silver\"])\n",
        "    metal_platinum = (main_metal == \"platinum\")\n",
        "    metal_silver = (main_metal == \"silver\")\n",
        "\n",
        "\n",
        "    # Jewelry category\n",
        "    category = st.selectbox(\"Category\", [\"necklace\", \"pendant\", \"ring\", \"souvenir\", \"stud\"])\n",
        "    cat_necklace = (category == \"necklace\")\n",
        "    cat_pendant = (category == \"pendant\")\n",
        "    cat_ring = (category == \"ring\")\n",
        "    cat_souvenir = (category == \"souvenir\")\n",
        "    cat_stud = (category == \"stud\")\n",
        "\n",
        "    # Brand selection\n",
        "    brand = st.selectbox(\"Brand\", [\"Brand 1\", \"Brand 2\", \"Brand 3\", \"Brand 4\", \"Brand 5\"])\n",
        "    brand_1 = (brand == \"Brand 1\")\n",
        "    brand_2 = (brand == \"Brand 2\")\n",
        "    brand_3 = (brand == \"Brand 3\")\n",
        "    brand_4 = (brand == \"Brand 4\")\n",
        "    brand_5 = (brand == \"Brand 5\")\n",
        "\n",
        "    # Create feature dictionary\n",
        "    features = {\n",
        "        'Year': year,\n",
        "        'Month': month,\n",
        "        'Hour': hour,\n",
        "        'Main_metal_platinum': metal_platinum,\n",
        "        'Main_metal_silver': metal_silver,\n",
        "        'Category_jewelry.necklace': cat_necklace,\n",
        "        'Category_jewelry.pendant': cat_pendant,\n",
        "        'Category_jewelry.ring': cat_ring,\n",
        "        'Category_jewelry.souvenir': cat_souvenir,\n",
        "        'Category_jewelry.stud': cat_stud,\n",
        "        'Brand_ID_1.0': brand_1,\n",
        "        'Brand_ID_2.0': brand_2,\n",
        "        'Brand_ID_3.0': brand_3,\n",
        "        'Brand_ID_4.0': brand_4,\n",
        "        'Brand_ID_5.0': brand_5\n",
        "    }\n",
        "\n",
        "    return pd.DataFrame(features, index=[0])\n",
        "\n",
        "def main():\n",
        "    st.title(\"Jewelry Price Prediction\")\n",
        "\n",
        "    input_df = user_input_features()\n",
        "\n",
        "    if st.button(\"Predict\"):\n",
        "        prediction = model.predict(input_df)\n",
        "        st.success(f\"Predicted Price: ${prediction[0]:.2f} USD\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ]
    }
  ]
}
