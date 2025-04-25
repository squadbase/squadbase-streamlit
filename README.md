# Squadbase Python SDK for Streamlit

SDK for streamlit to get user credentials in deployment environment on squadbase.

### Features

- Retrieve user information from Squadbase authentication API
- Support for local development with mock data
- Custom domain configuration

### Installation

```shell
pip install squadbase-streamlit
```

or with Poetry:

```shell
poetry add squadbase-streamlit
```

### Usage

#### In Squadbase Deployment Environment

When deployed on Squadbase, the SDK automatically extracts authentication information from the request headers:

```python
import streamlit as st
import squadbase.streamlit as sq

# Get Squadbase user information
user_info = sq.auth.get_user()

# Store in session state for reuse
st.session_state['user_info'] = user_info

# Access user data
st.write(f"Welcome, {user_info.get('firstName', '')} {user_info.get('lastName', '')}")
```

#### In Local Development Environment

For local development, you can use mock data to simulate the authentication:

```python
import streamlit as st
import squadbase.streamlit as sq

# Define mock user data for local testing
mock_user_data = {
    "username": "testuser",
    "firstName": "Test",
    "lastName": "User",
    "iconUrl": None,
    "email": "test@example.com",
    "role": ["Admin"]
}

# Get mock user information
user_info = sq.auth.get_user(mock_data=mock_user_data)

# Use the user information in your app
st.write(f"Hello, {user_info['firstName']} {user_info['lastName']}")
```
