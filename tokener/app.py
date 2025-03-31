import streamlit as st
import tiktoken
import json

# Pricing per 1000 tokens for GPT models
PRICING = {
    "gpt-4": {"input": 0.03, "output": 0.06},
    "gpt-3.5-turbo": {"input": 0.0015, "output": 0.002}
}

# Max token limits for models
TOKEN_LIMITS = {
    "gpt-4": 128000,
    "gpt-3.5-turbo": 16000
}

def count_tokens(text, model="gpt-4"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def calculate_cost(tokens, model, input_output="input"):
    cost_per_1000 = PRICING[model][input_output]
    return (tokens / 1000) * cost_per_1000

# Streamlit UI
st.title("Token and Cost Estimator")

# Sidebar with Model Info
st.sidebar.header("Model Info")
model_details = {
    "gpt-4": {"context_length": "128k tokens", "pricing": "$0.03 per 1k tokens (input) / $0.06 per 1k tokens (output)"},
    "gpt-3.5-turbo": {"context_length": "16k tokens", "pricing": "$0.0015 per 1k tokens (input) / $0.002 per 1k tokens (output)"}
}
selected_model = st.sidebar.selectbox("Choose a model:", ["gpt-4", "gpt-3.5-turbo"])
st.sidebar.write(f"**Context Length:** {model_details[selected_model]['context_length']}")
st.sidebar.write(f"**Pricing:** {model_details[selected_model]['pricing']}")

# User input for prompt
prompt = st.text_area("Enter your prompt:", height=200)

# Estimated completion length
completion_tokens = st.slider("Estimated completion length (in tokens):", 0, 2000, 100)

# Save and load history
if "prompt_history" not in st.session_state:
    st.session_state["prompt_history"] = []

if st.button("Save Prompt"):
    if prompt.strip():
        st.session_state["prompt_history"].append(prompt)
        st.success("Prompt saved!")

# Load prompt from history
if st.session_state["prompt_history"]:
    selected_prompt = st.selectbox("Load previous prompt:", st.session_state["prompt_history"], index=len(st.session_state["prompt_history"]) - 1)
    if st.button("Load Prompt"):
        prompt = selected_prompt

# Batch mode for CSV upload
uploaded_file = st.file_uploader("Upload a CSV of prompts for batch processing:", type=["csv"])

# Calculate tokens and costs
if st.button("Estimate Tokens and Cost"):
    if prompt.strip():
        num_tokens = count_tokens(prompt, selected_model)
        total_tokens = num_tokens + completion_tokens
        input_cost = calculate_cost(num_tokens, selected_model, "input")
        output_cost = calculate_cost(completion_tokens, selected_model, "output")
        total_cost = input_cost + output_cost

        # Token limit check
        if total_tokens > TOKEN_LIMITS[selected_model]:
            st.error(f"Total tokens ({total_tokens}) exceed the limit for {selected_model} ({TOKEN_LIMITS[selected_model]} tokens). Reduce the input or completion length.")
        else:
            st.write(f"### Token Breakdown")
            st.write(f"- Input Tokens: {num_tokens}")
            st.write(f"- Estimated Output Tokens: {completion_tokens}")
            st.write(f"- Total Tokens: {total_tokens}")
            st.write(f"### Estimated Cost")
            st.write(f"- Input Cost: ${input_cost:.4f}")
            st.write(f"- Output Cost: ${output_cost:.4f}")
            st.write(f"- Total Estimated Cost: ${total_cost:.4f}")
    else:
        st.warning("Please enter a valid prompt.")

# Batch processing logic
if uploaded_file is not None:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    if "prompt" in df.columns:
        df["tokens"] = df["prompt"].apply(lambda x: count_tokens(str(x), selected_model))
        df["input_cost"] = df["tokens"].apply(lambda x: calculate_cost(x, selected_model, "input"))
        st.write("### Batch Token and Cost Estimation")
        st.dataframe(df[["prompt", "tokens", "input_cost"]])
    else:
        st.error("CSV must contain a 'prompt' column.")
