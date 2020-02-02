#!/bin/bash

COLOR="\033[40m\033[32m"
UNCOLOR="\033[0m"

NAME=at

# only required if "anaconda" is not in the path
source $HOME/anaconda3/etc/profile.d/conda.sh

# conda create --yes -n $NAME python=3 ipdb bokeh jupyterlab ipywidgets ipycanvas nodejs -c defaults -c conda-forge
conda create --yes -n $NAME python=3 bokeh jupyterlab ipywidgets ipycanvas nodejs -c defaults -c conda-forge

conda activate $NAME

# ipycanvas
jupyter labextension install @jupyter-widgets/jupyterlab-manager ipycanvas

# bokeh
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install @bokeh/jupyter_bokeh

echo -e new environment is \"$COLOR$NAME$UNCOLOR\"

# the environment is exported into a yaml file
 conda env export --no-builds --from-history -f environment.yml
