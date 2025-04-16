import streamlit as st

import squadbase.streamlit as sq

# local sample data
mock_user_data = {
    "username": "testuser",
    "firstName": "Test",
    "lastName": "User",
    "iconUrl": None,
    "email": "test@example.com",
    "role": ["Admin"],
}

# get user information
user_info = sq.auth.get_user(mock_data=mock_user_data)

# show Streamlit app
st.title("Squadbase Streamlit Example")

st.write("## User Information")
st.json(user_info)

st.write("## Session State Example")
if "user_info" not in st.session_state:
    st.session_state["user_info"] = user_info
    st.success("Saved user information to session state")
else:
    st.info("User information already in session state")

st.write("User Information:", st.session_state["user_info"])
