# Prescriptive Watering: Data-Driven Optimization of Water Consumption in Kiwifruit Orchards

This repository contains the implementation of the following research paper:

- Baiardi Alex, Francia Matteo, Golfarelli Matteo, and Pasini Manuele. "Prescriptive Watering: Data-Driven Optimization of Water Consumption in Kiwifruit Orchards". Submitted to **Computers and Electronics in Agriculture** (2025) 

## Repository Description

The repository contains data and the processing pipeline to derive figures and statistics in the above research paper.

#### Data

- `data/field_data`: sensor data collected during the irrigation seasons.
- `data/experiments/pid_tuning/results/`: synthetic data obtained through running Auto-ML simulations on [Orchard-3DLab]([https://github.com/ManuelePasini/synthetic-soil-simulator/tree/pid_tuning](https://github.com/ftomei/Orchard-3DLab)). The data within this folder was leveraged in determining reference values for KP, KI in different scenarios (e.g., soil textures).
- `data/experiments/robustness`: synthetic data obtained through running Auto-ML simulations on [Orchard-3DLab]([https://github.com/ManuelePasini/synthetic-soil-simulator/tree/pid_tuning](https://github.com/ftomei/Orchard-3DLab)). The data within this folder was leveraged in assessing the robustness of SMARTER in different agricultural scenarios (different soil textures and irrigation frequnecies) and for comparing SMARTER with established precision irrigation techinques (ET0-based, Machine Learning-based)
  
#### Data processing pipelines

- `processing/CSAG_smart_irrigation.ipynb`: Python data pipeline to reproduce the article's figures and statistics from raw field data.
- `processing/PID_Tuning.ipynb`: Python data pipeline to reproduce the paper's figures related to tuning Kp and Ki PID parameters on different soil textures.
- `processing/ML_Training.ipynb`: Python data pipeline to reproduce the training of Gradient Boost Regression Trees models leveraged in the robustness tests.
- `processing/SMARTER_robustness.ipynb`: Python data pipeline to reproduce the paper's figures related to the robustness assessments of SMARTER.

### PI Controller - KP and KI reference values

- `docker-compose.yaml`: Docker compose file to reproduce the experiments for reference values of KP and KI and to run robustness tests.

### PI Controller - Assessing SMARTER robustness

- `docker-compose.yaml`: Docker compose file to reproduce the experiments for assessing the robustness of SMARTER and comparing it with two different irrigation strategies: evapotranspiration based (ET0) and machine learning based (Gradient Boost Regression Trees).

## Reproduce Experiments

The experiments need Python > 3 to run and some additional dependencies that can be found in `requirements.txt` file. There are two different ways to reproduce experiments: via shell or via IDE (e.g., Visual Studio Code).

### Data Generation

Experiments for reference values for KP and KP parameters within different soil textures scenarios (clay-loam, silty-loam, sandy-loam) can be reproduced through Docker and Orchard-3DLab.
- The Criteria2D repository and experiments setup for tuning KP and KI have been packed in a Docker image (the original repository is available at this link [this link](https://github.com/ManuelePasini/synthetic-soil-simulator/tree/pid_tuning)) runnable within this repository by opening a shell on this project root directory and running:
- The Criteria2D repository and experiments setup for assessing SMARTER robustness and performances against other precision irrigation techniques have been packed in a docker image in a Docker image (the original repository is available at this link [this link](https://github.com/ManuelePasini/synthetic-soil-simulator/tree/irrigation_strategies_comparison)) runnable within this repository by opening a shell on this project root directory and running:

```sh
docker compose up
```

Simulation results for each scenario will be available in the `data/experiments/pid_tuning/results/{scenario}/output` folder.

#### Visualize experimenst results 
Finally, to visualize such results, run the `processing/PID_Tuning.ipynb` notebook.

The simulation parameters can be found in the following directories:

- <b>Soil, crop and field parameters</b>: `data/experiments/pid_tuning_setup/{scenario}/data/{scenario}_{year}/settings`;
- <b>Weather parameters</b>: `data/experiments/pid_tuning_setup/{scenario}/data/{scenario}_{year}/meteo`.


### Data visualization

#### Shell

Dependencies can be installed via opening a shell within this repository's folder and running:

```sh
pip3 install -r requirements.txt
```

The experiments can then be run via opening the notebook itself or via running:

```sh
jupyter nbconvert --to notebook --execute processing/CSAG_smart_irrigation.ipynb --output results/CSAG_smart_irrigation_results.ipynb
jupyter nbconvert --to notebook --execute processing/PID_Tuning.ipynb --output results/PID_Tuning.ipynb
```

Alternatively, once the mandatory dependencies have been installed, notebooks can be run via a standard IDE (e.g., Visual Studio Code)

#### Docker (.devcontainer)

Opening the repository folder within an IDE (e.g., Visual Studio Code), it is possible to run the .devcontainer with all the mandatory libraries installed.
The two notebooks can the be run via IDE, or running the above shell commands within the container
