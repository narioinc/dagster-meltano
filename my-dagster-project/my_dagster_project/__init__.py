from dagster import Definitions, load_assets_from_modules, repository
from dagster_meltano import meltano_resource, meltano_run_op, load_jobs_from_meltano_project

from . import assets

all_assets = load_assets_from_modules([assets])
meltano_jobs = load_jobs_from_meltano_project("/home/narioinc/Documents/git_projects/dasgter-meltano/my-meltano-project")

defs = Definitions(
    assets=all_assets,
    jobs=meltano_jobs
)

@repository
def repository():
    return [meltano_jobs]
