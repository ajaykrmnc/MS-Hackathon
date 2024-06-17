import streamlit as st
import openai
from openai import AzureOpenAI

# Define constants
ENDPOINT = "https://polite-ground-030dc3103.4.azurestaticapps.net/api/v1"
API_KEY = "445dcfab-cbf2-463c-a733-b66c7dd8ba50"
API_VERSION = "2024-02-01"

# Define the model name
model_name = "gpt-35-turbo"

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

# Define the chatbot function
def chatbot():
    st.title("CureAI Chatbot")
    st.write("Welcome to CureAI chatbot. You can ask any health-related queries and get responses from the chatbot.")

    # Initialize session state to store messages if not already present
    if 'messages' not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": "You are a doctor and tell according to symptoms you have to tell which clinical test is necessary based on keywords and suggest what might cause this problem briefly in about 100 words and please don't help with any non health related query and keep asking the relevant question regarding the symptoms of the disease which the patient is suffering from till you won't get the right conclusion"}]

    # Input field for user message
    user_input = st.text_input("Your message:", key="user_input")

    if st.button("Send"):
        if user_input.strip() == "":
            st.warning("Please enter a message.")
        else:
            # Add the user's message to the conversation history
            st.session_state.messages.append({"role": "user", "content": user_input})

            try:
                # Generate the chatbot's response
                completion = client.chat.completions.create(
                    model=model_name,
                    messages=st.session_state.messages
                )

                # Extract the chatbot's response
                assistant_response = completion.choices[0].message.content

                # Add the chatbot's response to the conversation history
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            except Exception as e:
                st.error(f"An error occurred: {e}")

    # Display the conversation history
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"<div style='margin-bottom: 20px; text-align: right;'><span style='padding: 15px; background-color: #262630; border-radius: 20px; font-color: white;'>{message['content']}</span></div>", unsafe_allow_html=True)
        elif message["role"] == "assistant":
            st.markdown(f"**CureAI: 🤖** {message['content']}")

    st.markdown("---")

