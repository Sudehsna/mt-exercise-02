# MT Exercise 2: Pytorch RNN Language Models

This repo shows how to train neural language models using [Pytorch example code](https://github.com/pytorch/examples/tree/master/word_language_model). Thanks to Emma van den Bold, the original author of these scripts. 

# Requirements

- This only works on a Unix-like system, with bash.
- Python 3 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

# Steps

Clone this repository in the desired place:

    git clone https://github.com/marpng/mt-exercise-02
    cd mt-exercise-02

Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Download and install required software:

    ./scripts/install_packages.sh

Download and preprocess data:

    ./scripts/download_data.sh

Train a model:

    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved.

Generate (sample) some text from a trained model with:

    ./scripts/generate.sh


# Task 1:

We first modified the download_data.sh by renaming the URL and renamed all the files/folders to match our dataset.
We then proceeded to change the relevant paths to "moby" (our folder) and the epoch number in train.sh. While running we encountered a pickling error and changed the main.py and generate.py to inlcude the parameter weights_only=False for model = torch.load(...):

    ./scripts/download_data.sh

# Task 2:
 
Additional Flags:
The dropout setting we used are 0.0, 0.3, 0.5, 0.7, 0.9, which each need to be manually adapted during training.
In the main.py we added three additional flags --log-valid, --log-test and --log-epoch in train.sh to run the training with logging. We ran this script for each dropout setting to get the log-files:

    ./scripts/train.sh

The files will be stored in the new folder "logs" under the folder "data".
Since we have seperate .tsv files for each dropout setting and each perplexity we wrote a script (perplexity_table.py) that would concatenate the dropouts, epoch and perplexities depending on the type of perplexity (test, valid and epoch):

    python3 ./scripts/perplexity_table.py

To create the table and line chart we execute create_table.py and line_chart_plot.py which then stored in the folder tables_charts.

    python3 ./scripts/create_table.py
    python3 ./scripts/line_chart_plot.py

Finally, we generated two samples for the highest and lowest perplexity:

    ./scripts/generate.sh

Comment out the log-flags in train.sh to not append more data to the logging charts.  





(Hint: Name all the files the same as ours for the code to work without major changes :))
