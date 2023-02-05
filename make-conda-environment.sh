#!/bin/bash

NAME=at
MANAGER="mamba"

COLOR="\033[40m\033[32m"
UNCOLOR="\033[0m"

# only required if "anaconda" is not in the path
source $HOME/anaconda3/etc/profile.d/conda.sh

$MANAGER create --yes -n $NAME ipdb jupyterlab ipywidgets bokeh ipycanvas -c defaults -c conda-forge

echo -e new environment is \"$COLOR$NAME$UNCOLOR\"
