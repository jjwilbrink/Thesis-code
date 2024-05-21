# This is the repository for my thesis.

## Requirements

* fairseq 0.12.2
* matplotlib 3.8.4
* pandas 2.2.2

## Pipeline

1. Using ```preprocess_data.py```, the data from the SCAN dataset (in the SCAN/ folder) is preprocessed first to make sure everything is in the right format. The formatted data is put into the data folder.
2. Then, using ```preprocess_command.sh```, this data is further processed. This is a wrapper that calls the fairseq preprocess command for every datasplit. Because of the way fairseq functions, this is also the point where the distinction between the SCAN and NACS dataset is made. The processed data is saved in data-bin, which has a SCAN and a NACS subfolder, each containing a subfolder for every split.
3. This data is then used to train the models using ```train_command.sh```, which is a wrapper for the fairseq train command, including the right parameters. This command can also be called using ```sbatch_command.sh```, when using the slurm tool for running the training tasks.
4. Output can be generated using ```generate_command.sh```, which is again a wrapper. Generated outputs i put into the outputs folder.
5. The raw generated output is further processed using ```scoring.py```, and the outputs are saved in the processed_outputs folder
6. These outputs are analysed using the ```stats.ipynb``` notebook, which directly shows the generated plots as well as saving the image files.
