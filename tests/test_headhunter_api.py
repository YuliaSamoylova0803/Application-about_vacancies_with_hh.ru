import unittest
from unittest.mock import MagicMock, patch

from src.headhunter_api import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    @patch("src.headhunter_api.requests.get")
    def test_load_vacancies(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "items": [{"name": "Python Developer", "salary": "1000"}, {"name": "Data Scientist", "salary": "1500"}]
        }
        mock_get.return_value = mock_response
        hh = HeadHunterAPI()
        hh._load_vacancies("Python Developer")
        self.assertGreater(len(hh.vacancies), 0)
        self.assertEqual(hh.vacancies[0]["name"], "Python Developer")

        mock_get.assert_called_with(
            "https://api.hh.ru/vacancies",
            headers={"User-Agent": "HH-User-Agent"},
            params={"text": "Python Developer", "page": 10, "per_page": 100},
        )


if __name__ == "__main__":
    unittest.main()
