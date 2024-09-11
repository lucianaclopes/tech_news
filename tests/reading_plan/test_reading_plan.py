from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from unittest.mock import patch
import pytest


def test_reading_plan_group_news():
    # Arrange
    mock_news = [
        {"title": "Notícia bacana", "reading_time": 4},
        {"title": "Notícia bacana 2", "reading_time": 1},
        {
            "title": "Nuvem híbrida: o que é, quais os tipos e quando usar?",
            "reading_time": 8,
        },
        {
            "title": "Memória cache: o que é, como funciona e cache vs RAM!",
            "reading_time": 6,
        },
        {
            "title":
            "Daily Scrum: o que é, como fazer e importância na gestão ágil!",
            "reading_time": 8,
        },
        {
            "title": "Por onde começar a estudar programação para iniciantes?",
            "reading_time": 14,
        },
        {
            "title":
            "Kanban: o que é, como funciona e como aplicar esse método?",
            "reading_time": 12,
        },
    ]

    with patch("tech_news.database.find_news", return_value=mock_news):
        # Act
        result = ReadingPlanService.group_news_for_available_time(15)

        # Assert
        expected_result = {
            "readable": [
                {
                    "unfilled_time": 2,
                    "chosen_news": [
                        ("Notícia bacana", 4),
                        ("Notícia bacana 2", 1),
                        (
                            "Nuvem híbrida: o que é, quais os tipos e quando "
                            "usar?",
                            8,
                        ),
                    ],
                },
                {
                    "unfilled_time": 1,
                    "chosen_news": [
                        (
                            "Memória cache: o que é, como funciona e cache vs "
                            "RAM!",
                            6,
                        ),
                        (
                            "Daily Scrum: o que é, como fazer e importância "
                            "na gestão ágil!",
                            8,
                        ),
                    ],
                },
                {
                    "unfilled_time": 1,
                    "chosen_news": [
                        (
                            "Por onde começar a estudar programação para "
                            "iniciantes?",
                            14,
                        ),
                    ],
                },
                {
                    "unfilled_time": 3,
                    "chosen_news": [
                        (
                            "Kanban: o que é, como funciona e como aplicar "
                            "esse método?",
                            12,
                        ),
                    ],
                },
            ],
            "unreadable": [],
        }

        assert result == expected_result

        # Teste de exceção para valor inválido
        with pytest.raises(ValueError):
            ReadingPlanService.group_news_for_available_time(-1)
