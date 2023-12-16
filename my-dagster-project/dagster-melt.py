from dagster import repository, job, Definitions
from dagster_meltano import load_jobs_from_meltano_project, meltano_resource, meltano_run_op

meltano_jobs = load_jobs_from_meltano_project("/home/narioinc/Documents/git_projects/dasgter-meltano/my-meltano-project")



@job(resource_defs={"meltano": meltano_resource})
def meltano_run_job():
    tap_done = meltano_run_op("tap-github target-jsonl")()
    #meltano_run_op("tap-github")(tap_done)

@repository
def repository():
    return [meltano_run_job]

defs = Definitions(jobs=[meltano_run_job])