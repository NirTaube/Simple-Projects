# Token and Cost Estimator

![Streamlit](https://img.shields.io/badge/Streamlit-1.0-red?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

## 📢 **Description**

The **Token and Cost Estimator** is a Streamlit-powered application that calculates token usage and estimated cost for different OpenAI models (`gpt-4` and `gpt-3.5-turbo`). It helps developers optimize their prompts and control costs by providing real-time token analysis and breakdowns. The app also supports batch processing via CSV uploads and stores prompt history for easy reference.

### ⚡ **Why Use This App?**
- Save time by estimating API costs before running heavy prompts.
- Prevent token overages by keeping track of prompt and completion lengths.
- Compare token costs between models to choose the best one for your task.

## 📚 **Features**
- **Input + Output Estimation** – Calculates token count and cost for both input and estimated output length.
- **Token Limit Warnings** – Alerts when token usage exceeds the model's maximum limit.
- **Save & Load Prompt History** – Allows saving and loading of previous prompts.
- **Batch Mode (CSV Upload)** – Upload a CSV with prompts and estimate tokens and costs in bulk.
- **Model Info Sidebar** – Displays token limits and cost details for the selected model.

## 🚀 **Getting Started**

### 1. **Clone the Repository**


### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3. **Run the Streamlit App**
```bash
streamlit run app.py
```

## 📦 **Requirements**

The required Python packages are listed in `requirements.txt`:
```
streamlit
pandas
tiktoken
```

## 📊 **How It Works**

### Input Section
- Enter your prompt in the text area.
- Choose a model (`gpt-4` or `gpt-3.5-turbo`).
- Set the estimated completion length (optional).

### Token and Cost Estimation
- Click **"Estimate Tokens and Cost"** to calculate token count and cost.
- View detailed breakdown and cost summary.

### Save & Load Prompt History
- Click **"Save Prompt"** to save the current prompt.
- Load previous prompts using the dropdown and load button.

### Batch Mode for CSV
- Upload a CSV file with a `prompt` column.
- View token and cost estimation for all prompts.

## 📝 **Notes**
- Token limits: 128k for `gpt-4` and 16k for `gpt-3.5-turbo`.
- Costs are estimated based on OpenAI's pricing per 1000 tokens.

## 📧 **Support**
For any questions or issues, feel free to contact the repository maintainer.

