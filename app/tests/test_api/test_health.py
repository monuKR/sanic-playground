import pytest


class TestHealth:

    @pytest.mark.asyncio
    async def test_health(self, test_client):
        _, response = await test_client.get('/ping')

        assert response.status_code == 200
        assert response.json == {'ping': 'pong'}
