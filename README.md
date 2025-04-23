# Squadbase Python SDK for Streamlit

SDK for streamlit to get user credentials in deployment environment on squadbase.

## Installation

```shell
$ pip install squadbase-streamlit
```

## Usage

```python
import streamlit as st
import squadbase.streamlit as sq

# get squadbase user infomation
st.session_state['user_info'] = sq.auth.get_user()

# use mock data in local env
st.session_state['user_info'] = sq.auth.get_user(mock_data={
    "username": "testuser",
    "firstName": "Test",
    "lastName": "User",
    "iconUrl": None,
    "email": "test@example.com",
    "role": ["Admin"]
})
```
