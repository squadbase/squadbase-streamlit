import json
from logging import getLogger
from typing import Any, Dict, Optional

import requests

_logger = getLogger(__name__)


def get_user(
    mock_data: Optional[Dict[str, Any]] = None,
    custom_domain: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Retrieve user information from Squadbase API

    @param mock_data: Optional mock data to return instead of making API call.
    @param custom_domain: Optional custom domain to use instead of default domain.
    """

    if mock_data is not None:
        return mock_data

    try:
        import streamlit as st

        headers = getattr(st.context, "headers", None)
        if headers:
            headers = {key.lower(): value for key, value in headers.items()}
    except ImportError:
        _logger.warning("Streamlit not found, using default headers.")
        headers = None

    host = _get_host_from_headers(headers)

    if host == "localhost":
        _logger.warning("Running on localhost, skipping squadbase authentication.")
        return {}

    subdomain = _extract_subdomain(host)
    if not subdomain:
        _logger.warning("No subdomain found in host.")
        return {}

    cookies = _get_cookies_from_headers(headers)

    return _call_auth_api(subdomain, cookies, custom_domain)


def _get_host_from_headers(headers: Optional[Dict[str, str]]) -> str:
    if not headers:
        return "localhost"

    host = headers.get("host", "") or headers.get("Host", "")
    return host.lower() if host else "localhost"


def _extract_subdomain(host: str) -> str:
    if host == "localhost":
        return ""

    parts = host.split(".")
    if len(parts) >= 3:
        return parts[0]
    return ""


def _get_cookies_from_headers(headers: Optional[Dict[str, str]]) -> Dict[str, str]:
    if not headers:
        return {}

    result = {}
    cookie_str = headers.get("cookie", "") or headers.get("Cookie", "")
    if cookie_str:
        result["cookie"] = cookie_str
    else:
        _logger.warning("No authorization value found in headers.")

    return result


def _call_auth_api(
    subdomain: str, headers: Dict[str, str], custom_domain: Optional[str] = None
) -> Dict[str, Any]:
    if custom_domain:
        url = f"https://{subdomain}.{custom_domain}/_sqcore/auth"
    else:
        url = f"https://{subdomain}.squadbase.app/_sqcore/auth"

    try:
        response = requests.post(url=url, headers=headers, timeout=10)

        if response.status_code == 200:
            return response.json()  # type: ignore
        else:
            _logger.warning(f"API call failed with status code {response.status_code}")
    except (requests.RequestException, json.JSONDecodeError) as e:
        _logger.error(f"Error during API call: {e}")
        pass

    return {}
