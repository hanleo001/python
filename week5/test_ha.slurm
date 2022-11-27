#! /bin/bash

#SBATCH --job-name=test_hh
#SBATCH --partition=64c512g
#SBATCH -n 1
#SBATCH --ntasks-per-node=1
#SBATCH --output=he.out
#SBATCH --error=all.err

module load miniconda3

python lesson_1.py