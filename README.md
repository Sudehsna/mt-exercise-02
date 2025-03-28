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

**Note task 1**:
We used Nathan the Wise as new dataset for training the model.
We modified download_data.sh by changing the url, the names and the path of the files.
First tried using Nathan The Wise and perplexity stayed high for the last 10+ epochs. Which means the hyperparamters were not optimal and or the text was not suitable for this kind of model training (i.e. too short). There might also have been some issues with formatting the text. To combat the potentiall limiation of the text length we tried Moby Dicks The Whale to bypass the shortness of Nathan The Wise. But even here we see that the perplexity has not significantly decreased in the last something epochs which lead us to blieve that it indeed is the hyperparameter setting which causes these issues. Both text produced gibberish text samples but we can clearly see that it has been trained on the specified text since we see words like "Whale" appearing which seem very specific to the text. 
**Notes task 2**:

