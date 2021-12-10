import os
import shutil

from catkin_tools.execution.jobs import Job
from catkin_tools.execution.stages import FunctionStage, CommandStage
from catkin_tools.jobs.utils import loadenv, makedirs


def symlink_package(logger, event_queue, src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.islink(dst):
        if not os.path.samefile(src, dst):
            os.remove(dst)
    elif os.path.isfile(dst) and not os.path.samefile(src, dst):
        os.remove(dst)
    elif os.path.isdir(dst) and not os.path.samefile(src, dst):
        shutil.rmtree(dst)
    if not os.path.exists(dst):
        os.symlink(src, dst)

    return 0


def create_ament_python_build_job(context, package, package_path, dependencies, **kwargs):
    # Package source space path
    pkg_dir = os.path.join(context.source_space_abs, package_path)

    # Environment dictionary for the job, which will be built
    # up by the executions in the loadenv stage.
    job_env = dict(os.environ)

    dest_path = context.package_dest_path(package)
    dest_python_path = os.path.join(dest_path, 'lib', 'python3', 'dist-packages')

    # Create job stages
    stages = []

    stages.append(FunctionStage(
        'symlink',
        symlink_package,
        src=os.path.join(pkg_dir, package.name),
        dst=os.path.join(dest_python_path, package.name),
    ))

    return Job(
        jid=package.name,
        deps=dependencies,
        env=job_env,
        stages=stages,
    )


description = dict(
    build_type='ament_python',
    description="Builds a package with ament_python build type",
    create_build_job=create_ament_python_build_job,
)
