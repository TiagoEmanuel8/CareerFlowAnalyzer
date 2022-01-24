from src.jobs import read


def get_unique_job_types(path):
    filterJob = list([jobs['job_type'] for jobs in read(path)])
    return set(filterJob)
