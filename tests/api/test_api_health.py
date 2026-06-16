import requests
from config.config import BASE_URL


class TestAPIHealth:

    def test_api_returns_200(self):
        """Verify API endpoint returns 200 status"""
        response = requests.get(f"{BASE_URL}/api/health")
        assert response.status_code == 200

    def test_api_response_is_json(self):
        """Verify API response is in JSON format"""
        response = requests.get(f"{BASE_URL}/api/health")
        assert response.headers["Content-Type"] == "application/json"

    def test_api_response_time(self):
        """Verify API responds within 3 seconds"""
        response = requests.get(f"{BASE_URL}/api/health")
        assert response.elapsed.total_seconds() < 3
