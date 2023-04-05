#!/bin/bash
#SBATCH --job-name=python_job
#SBATCH --output=python_job.out
#SBATCH --error=python_job.err
#SBATCH --partition=test
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:10:00

python3 test.py
