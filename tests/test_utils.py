from src.utils import connect_to_db
import pytest
from unittest.mock import patch

@pytest.fixture
def mock_env():
    env_vars = {
        'PG_USERNAME': 'abc'
    }
    with patch.dict('os.environ', env_vars) as mock_env:
        yield mock_env

# needs mock db adding
@patch('src.utils', autospec=True)
def test_connect_to_db_creates_connection(mock_conn, mock_env):
    connect_to_db()
    mock_conn.assert_called_with(
        dbname='test_db',
        user='abc'
    )