import streamlit as st

def chatbot(client, model_name):
    st.title("CureAI chatbot")
    st.write("Welcome to CureAI chatbot. You can ask any health-related queries and get responses from the chatbot.")
    
    user_input = st.text_input("", key="user_input", value="", max_chars=None, help=None)
    
    if st.button("Send"):
        if user_input.strip() == "":
            st.warning("Please enter a message.")
        else:
            messages = [{"role": "system", "content": "You are a doctor and tell according to symptoms you have to tell which clinical test is necessary based on keywords and suggest what might cause this problem briefly in about 100 words"}]
            messages.append({"role": "user", "content": user_input})

            completion = client.chat.completions.create(model=model_name, messages=messages)

            assistant_response = completion.choices[0].message.content
            messages.append({"role": "assistant", "content": assistant_response})

            for message in messages:
                if message["role"] == "assistant":
                    st.write("", message["content"])
    
    st.markdown("---")
