from jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs = read(path)

    filtered_jobs = set()

    [filtered_jobs.add(el['job_type']) for el in jobs if el['job_type'] != ""]

    # print(type_jobs)

    return filtered_jobs


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type
    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter
    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filter_job = [
        el for el in jobs if el['job_type'] == job_type
    ]

    # print(type_jobs)

    return filter_job


def get_unique_industries(path):
    """Checks all different industries and returns a list of them
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    list
        List of unique industries
    """
    jobs = read(path)

    type_industries = set()

    [
        type_industries.add(el['industry'])
        for el in jobs
        if el['industry'] != ''
    ]

    # print(type_industries)

    return type_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry
    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter
    Returns
    -------
    list
        List of jobs with provided industry
    """
    industries = set()

    [
        industries.add(el['industry'])
        for el in jobs
        if el['industry'] == industry
    ]

    # print(industries)

    return industries


def get_max_salary(path):
    """Get the maximum salary of all jobs
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs = read(path)

    salaries = set()

    [salaries.add(int(el['max_salary'])) for el in jobs]

    # print(salaries)

    # print(max(salaries))

    return max(salaries)


def get_min_salary(path):
    """Get the minimum salary of all jobs
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs = read(path)

    salaries = set()

    [salaries.add(int(el['min_salary'])) for el in jobs]

    # print(salaries)

    # print(min(salaries))

    return min(salaries)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job
    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job
    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise
    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if (
        # caso o campo salário não seja inteiro
        type(salary) != int
            # caso os campos não sejam passados
            or "min_salary" not in job
            or "max_salary" not in job
            # caso os campos salários não sejam do tipo inteiro
            or type(job["min_salary"]) != int
            or type(job["max_salary"]) != int
            # caso o valor mínimo seja maior que o salário máximo
            or job["min_salary"] > job["max_salary"]):

        raise ValueError("Value Error")

    salary = (job["max_salary"] >= salary >= job["min_salary"])

    return salary


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range
    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter
    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    # filtered_salary_range = []
    # for job in jobs:
    #     if (
    #         isinstance(salary, int)
    #         and isinstance(job["min_salary"], int)
    #         and isinstance(job["max_salary"], int)
    #     ):
    #         if job["min_salary"] <= salary <= job["max_salary"]:
    #             filtered_salary_range.append(job)
    # return filtered_salary_range
