from src.sorting import sort_by


mock = [
    {
        "min_salary": 500,
        "max_salary": 1500,
        "date_posted": "2021-01-31",
    },
    {
        "min_salary": 1000,
        "max_salary": 2500,
        "date_posted": "2021-01-30",
    },
    {
        "min_salary": 1500,
        "max_salary": 3000,
        "date_posted": "2021-01-29",
    }
]

ordered_date = [
    mock[2], mock[1], mock[0]
]

ordered_min_salary = [
    mock[0], mock[1], mock[2]
]

ordered_max_salary = [
    mock[0], mock[1], mock[2]
]

criterios = ["date_posted", "max_salary", "min_salary"]


def test_sort_by_criterios():
    # testando a data
    sort_by(mock, criterios[0])
    assert mock == ordered_date

    # teste de salário máximo
    sort_by(mock, criterios[1])
    assert mock == ordered_max_salary

    # teste de salário mínimo
    sort_by(mock, criterios[2])
    assert mock == ordered_min_salary
