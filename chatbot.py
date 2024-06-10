import streamlit as st

# Define the chatbot function
def chatbot(client, model_name):
    st.title("💬 CureAI Chatbot")
    st.write(" 🚀 Welcome to CureAI chatbot. You can ask any health-related queries and get responses from the chatbot.")

    # Initialize session state to store messages if not already present
    if 'messages' not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": "You are a doctor and tell according to symptoms you have to tell which clinical test is necessary based on keywords and suggest what might cause this problem briefly in about 100 words and please don't help with any non health related query"}]
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""

    # Create a container for the conversation history
    chat_container = st.container()
    with chat_container:
        # Display the conversation history
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"**You:** {message['content']}")
            elif message["role"] == "assistant":
                st.markdown(f"**CureAI:** {message['content']}")
        st.markdown("---")

    # Input bar at the bottom of the screen
    input_container = st.container()
    with input_container:
        user_input = st.text_input("Your message:", key="user_input")
        if st.button("Send"):
            if user_input.strip() == "":
                st.warning("Please enter a message.")
            else:
                # Add the user's message to the conversation history
                st.session_state.messages.append({"role": "user", "content": user_input})

                # Generate the chatbot's response
                completion = client.chat.completions.create(
                    model=model_name,
                    messages=st.session_state.messages
                )

                # Extract the chatbot's response
                assistant_response = completion.choices[0].message.content

                # Add the chatbot's response to the conversation history
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})

                # Clear the input field after sending the message
                st.session_state.user_input = ""

