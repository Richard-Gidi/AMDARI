{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO4Nq1j8Ih62OOQlpf56zY4",
      "include_colab_link": true
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
        "<a href=\"https://colab.research.google.com/github/Richard-Gidi/AMDARI/blob/main/stream.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
      "execution_count": 3,
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
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Load the trained model\n",
        "model = joblib.load('models/jewelry_price_optimizer.pkl')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 304
        },
        "id": "oXkrSoM3MQeY",
        "outputId": "326f8238-1dc3-4a54-940e-5aa3be3c6675"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ValueError",
          "evalue": "EOF: reading array data, expected 262144 bytes got 165904",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-8-76a730c650f1>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# Load the trained model\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mmodel\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mjoblib\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mload\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'jewelry_price_rf.joblib'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/joblib/numpy_pickle.py\u001b[0m in \u001b[0;36mload\u001b[0;34m(filename, mmap_mode)\u001b[0m\n\u001b[1;32m    656\u001b[0m                     \u001b[0;32mreturn\u001b[0m \u001b[0mload_compatibility\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfobj\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    657\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 658\u001b[0;31m                 \u001b[0mobj\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_unpickle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfilename\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmmap_mode\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    659\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/joblib/numpy_pickle.py\u001b[0m in \u001b[0;36m_unpickle\u001b[0;34m(fobj, filename, mmap_mode)\u001b[0m\n\u001b[1;32m    575\u001b[0m     \u001b[0mobj\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    576\u001b[0m     \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 577\u001b[0;31m         \u001b[0mobj\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0munpickler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mload\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    578\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0munpickler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcompat_mode\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    579\u001b[0m             warnings.warn(\"The file '%s' has been generated with a \"\n",
            "\u001b[0;32m/usr/lib/python3.11/pickle.py\u001b[0m in \u001b[0;36mload\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   1211\u001b[0m                     \u001b[0;32mraise\u001b[0m \u001b[0mEOFError\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1212\u001b[0m                 \u001b[0;32massert\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbytes_types\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1213\u001b[0;31m                 \u001b[0mdispatch\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1214\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0m_Stop\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mstopinst\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1215\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mstopinst\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvalue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/joblib/numpy_pickle.py\u001b[0m in \u001b[0;36mload_build\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    413\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0marray_wrapper\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mNDArrayWrapper\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    414\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcompat_mode\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 415\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstack\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0marray_wrapper\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    416\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    417\u001b[0m     \u001b[0;31m# Be careful to register our new method.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/joblib/numpy_pickle.py\u001b[0m in \u001b[0;36mread\u001b[0;34m(self, unpickler)\u001b[0m\n\u001b[1;32m    250\u001b[0m             \u001b[0marray\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_mmap\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0munpickler\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    251\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 252\u001b[0;31m             \u001b[0marray\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_array\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0munpickler\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    253\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    254\u001b[0m         \u001b[0;31m# Manage array subclass case\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/joblib/numpy_pickle.py\u001b[0m in \u001b[0;36mread_array\u001b[0;34m(self, unpickler)\u001b[0m\n\u001b[1;32m    175\u001b[0m                 \u001b[0mread_count\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmax_read_count\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcount\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    176\u001b[0m                 \u001b[0mread_size\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mread_count\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdtype\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mitemsize\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 177\u001b[0;31m                 data = _read_bytes(unpickler.file_handle,\n\u001b[0m\u001b[1;32m    178\u001b[0m                                    read_size, \"array data\")\n\u001b[1;32m    179\u001b[0m                 \u001b[0marray\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0mi\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mread_count\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m\u001b[0;31m \u001b[0m\u001b[0;31m\\\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/joblib/numpy_pickle_utils.py\u001b[0m in \u001b[0;36m_read_bytes\u001b[0;34m(fp, size, error_template)\u001b[0m\n\u001b[1;32m    249\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0msize\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    250\u001b[0m         \u001b[0mmsg\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"EOF: reading %s, expected %d bytes got %d\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 251\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmsg\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0merror_template\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msize\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    252\u001b[0m     \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    253\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mValueError\u001b[0m: EOF: reading array data, expected 262144 bytes got 165904"
          ]
        }
      ]
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
        "    # Main gem selection\n",
        "    gem = st.selectbox(\"Main Gem\", [\"None\", \"amber\", \"amethyst\", \"chrysolite\", \"chrysoprase\"])\n",
        "    gem_amber = (gem == \"amber\")\n",
        "    gem_amethyst = (gem == \"amethyst\")\n",
        "    gem_chrysolite = (gem == \"chrysolite\")\n",
        "    gem_chrysoprase = (gem == \"chrysoprase\")\n",
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
        "        'Main_gem_amber': gem_amber,\n",
        "        'Main_gem_amethyst': gem_amethyst,\n",
        "        'Main_gem_chrysolite': gem_chrysolite,\n",
        "        'Main_gem_chrysoprase': gem_chrysoprase,\n",
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