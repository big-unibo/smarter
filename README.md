# Prescriptive Smart Watering: Automatic Optimization of Water Consumption and Fruit Quality in Orchards

## Research papers

This repository contains the implementation of the following research paper:

- Baiardi Alex, Francia Matteo, Golfarelli Matteo, and Pasini Manuele. "Prescriptive Smart Watering: Automatic Optimization of Water Consumption and Fruit Quality in Orchards". Submitted to **Computers and Electronics in Agriculture** (2025) 

## Repository Description
The repository contains data and the processing pipeline to derive figures and statistics in the above research paper.
#### Data
- /data/field_data: sensor data extracted for evaluating SMARTER.
- /data/tuning: synthetic data obtained through running Auto-ML simulations on (https://github.com/josephgiovanelli/synthetic-soil-simulator/tree/pid_tuning)[CRITERIA-2D]. The data within this folder was leveraged in determining starting values for Kp, Ki in different soil textures.
#### Data processing pipelines
- CSAG_smart_irrigation.ipynb: Python data pipeline to reproduce the article's figures from raw field data
- PID_Tuning.ipynb: Python data pipeline to reproduce the article's figures related to tuning Kp and Ki PID parameters on different soil textures

## Reproduce Experiments
The experiments need Python > 3 to run and some additional dependencies that can be found in `requirements.txt` file. There are two different ways to reproduce experiments.

### Shell
Dependencies can be installed via opening a shell within this repository's folder and running
```sh
  pip3 install -r requirements.txt
```
The experiments can then be run via opening the notebook itself or via running:
```sh
  jupyter nbconvert --to notebook --execute CSAG_smart_irrigation.ipynb --output results/CSAG_smart_irrigation_results.ipynb
  jupyter nbconvert --to notebook --execute PID_Tuning.ipynb --output results/PID_Tuning.ipynb
```

Alternatively, once the mandatory dependencies have been installed, notebooks can be run via a standard IDE (e.g., Visual Studio Code)

### Docker (.devcontainer)
Opening the repository folder within an IDE (e.g., Visual Studio Code), it is possible to run the .devcontainer with all the mandatory libraries installed.
The two notebooks can the be run via IDE, or running the above shell commands within the container
