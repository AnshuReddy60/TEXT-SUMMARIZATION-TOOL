# TEXT-SUMMARIZATION-TOOL

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: ANSHU VEERAMALLA

**INTERN ID**: CODF269

**DOMAIN**: AIML(ARTIFICIAL INTELLIGENCE MARKUP LANGUAGE)

**DURATION**: 1 MONTH

**MENTOR**: NEELA SANTOSH

# DESCCRIPTION

This **Text Summarization Tool** is a web-based application developed using **Streamlit** and **Hugging Face's Transformers** library. The tool allows users to upload or paste long text and generate concise, meaningful summaries using advanced **Natural Language Processing (NLP)** techniques. It is ideal for anyone who needs to quickly summarize lengthy documents such as articles, research papers, and reports.

### **Overview**

The core of this application leverages **Hugging Face's pre-trained transformer models** like **BART** and **T5** for abstractive text summarization. These models are capable of understanding the context of input text and generating concise summaries that retain the key ideas. The tool is built with **Streamlit**, providing an intuitive, interactive interface for users.

### **Key Features**

- **Text Input**: Users can paste their text directly into the application or upload a text file for summarization.
- **Summary Length Control**: Users can control the maximum length of the summary (in tokens), adjusting the level of detail required.
- **Abstractive Summarization**: The tool uses advanced transformer models to generate human-like summaries based on the input text.
- **Downloadable Summary**: Once the summary is generated, users can download it as a **.txt** file for offline use.
  
### **How It Works**

1. **Input Text**: Users paste the text or upload a file.
2. **Set Summary Length**: Users specify the maximum summary length in tokens. The minimum length is automatically adjusted based on the maximum length.
3. **Summarize**: After clicking "Summarize Now", the model processes the input and generates the summary.
4. **Download Summary**: The generated summary can be downloaded as a **.txt** file.

### **Technologies Used**

- **Streamlit**: An open-source app framework for building interactive applications with minimal code.
- **Hugging Face Transformers**: A library for accessing pre-trained models like **BART** and **T5** for text generation tasks.
- **Python**: The entire tool is built in Python, which is widely used in NLP and machine learning projects.
- **io**: Used to generate downloadable summary files.

### **How to Run the Application**

#### **1. Install Required Libraries**

To run the application, first install the required libraries by running the following command in your terminal or command prompt:

```bash
pip install streamlit transformers torch
```

This will install **Streamlit** (for building the web interface), **Transformers** (for the pre-trained models), and **Torch** (for running the models).

#### **2. Clone or Download the Project Files**

You can either clone the repository or download the project files directly to your local machine. If you're using the file upload feature, make sure the project includes the necessary code to handle file inputs.

#### **3. Run the Streamlit App**

Once you have the dependencies installed and the files ready, run the following command to launch the app:

```bash
streamlit run text_summarization_app.py
```

This will start the Streamlit server and open the app in your default browser. If everything is set up correctly, you should see the **Text Summarization Tool** interface.

#### **4. Use the Application**

- Paste or upload a lengthy article or text into the provided input field.
- Adjust the maximum summary length using the slider.
- Click "Summarize Now" to generate the summary.
- Download the summary as a **.txt** file using the download button.

### **Conclusion**

The **Text Summarization Tool** simplifies the task of condensing long-form content into concise summaries using state-of-the-art transformer models. Built with **Streamlit** and **Hugging Face**, this tool demonstrates the power of **abstractive summarization** in modern NLP applications. It is a great tool for content curators, researchers, and anyone who needs to process large amounts of text quickly and effectively.

## OUTPUT

![Image](https://github.com/user-attachments/assets/dba7ecf5-8612-4605-84b3-2ddd80518d82)

![Image](https://github.com/user-attachments/assets/fbe032ac-6559-4be8-93a5-bada7f5f0ae0)

