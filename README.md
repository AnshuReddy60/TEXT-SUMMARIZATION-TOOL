# TEXT-SUMMARIZATION-TOOL

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: ANSHU VEERAMALLA

**INTERN ID**: CODF269

**DOMAIN**: AIML(ARTIFICIAL INTELLIGENCE MARKUP LANGUAGE)

**DURATION**: 1 MONTH

**MENTOR**: NEELA SANTOSH

# DESCCRIPTION

### 📄 Text Summarization Tool – Internship at CodTech

This project is developed as part of my internship at **CodTech**, where I built a **Text Summarization Tool** using **Streamlit** and **Hugging Face Transformers**. The primary goal of this tool is to help users quickly generate concise summaries from long text, enhancing information consumption and helping users save time by condensing lengthy articles into key insights.

The Text Summarization Tool leverages **Natural Language Processing (NLP)** techniques to automatically generate summaries. It is designed to be simple, intuitive, and fast, making it a useful application for professionals, researchers, and content creators who need to summarize articles, reports, or other text-heavy documents.

### **Key Features:**

- **Interactive UI**: Built with **Streamlit**, this tool provides an easy-to-use interface where users can paste their article and control the summary length dynamically.
- **Text Summarization**: Using pre-trained **transformer models** (like BART and T5), the tool can perform **abstractive summarization** by understanding the context of the input text and generating meaningful, human-like summaries.
- **Download Option**: Once the summary is generated, users have the option to download it as a `.txt` file, making it easy to save and share the results.
- **Dynamic Length Control**: Users can control the length of the generated summary by adjusting the maximum token length, providing flexibility for various use cases.

### **Implementation Details:**

- **Streamlit**: The app is built using Streamlit to provide a web-based, user-friendly interface. Streamlit makes it easy to deploy the summarizer and allows for rapid prototyping, so users can interact with the model directly in their browser.
- **Transformers Library**: The tool uses the **Hugging Face Transformers** library to load a pre-trained **summarization pipeline**. The pipeline is fine-tuned for text summarization tasks and performs efficiently on articles of varying lengths.
- **Caching with `st.cache_resource`**: The summarization pipeline is cached using Streamlit's `@st.cache_resource` decorator, ensuring that the model is loaded only once during the app's session, leading to faster response times.
- **Text Preprocessing**: The input text undergoes basic processing, including validation to ensure that the text is sufficiently long (at least 50 words) for summarization.
- **Summary Length Control**: Users can set the maximum and minimum lengths for the generated summary. The tool adjusts the `min_length` dynamically based on the `max_length` to ensure that summaries are concise yet informative.

### **How It Works:**

1. **User Input**: Users paste their article or text into the provided input field.
2. **Adjust Summary Length**: Users can adjust the desired summary length by selecting the maximum length (in tokens). The minimum length is automatically set to 50% of the maximum length.
3. **Generate Summary**: Once the user clicks the "Summarize Now" button, the tool processes the input text, generates the summary using the transformer model, and displays the result.
4. **Download Summary**: After the summary is displayed, users can download it as a `.txt` file.

### **Technologies Used:**

- **Streamlit**: For building the interactive user interface.
- **Hugging Face Transformers**: For leveraging pre-trained models like BART and T5 for summarization.
- **Python**: The entire application is built using Python for backend processing.
- **io**: To generate downloadable summary files.

### **Conclusion:**

This Text Summarization Tool is a practical solution for anyone looking to quickly summarize lengthy documents. The tool demonstrates how cutting-edge NLP techniques can be used to make information more accessible. It also reflects my learning and hands-on experience during my internship at CodTech, where I applied my skills in **Python**, **NLP**, and **web app development** to create a useful, real-world tool.

## OUTPUT

![Image](https://github.com/user-attachments/assets/6a631d4c-3955-4fd6-9579-0c97780f42b3)

![Image](https://github.com/user-attachments/assets/b849312f-5bcc-418a-875e-1e3e85b62212)

