#! /bin/bash

#SBATCH --job-name=test_hh1
#SBATCH --partition=64c512g
#SBATCH -n 1
#SBATCH --ntasks-per-node=1
#SBATCH --output=1.out
#SBATCH --error=1.err

module load miniconda3

python /dssg/home/acct-stu/stu1373/py/week5/lesson_1.py
