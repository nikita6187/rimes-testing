#!/bin/bash

export PATH=~/cuda-9.0/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/cuda-9.0/extras/CUPTI/lib64
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/cuda-9.0/lib64

source ./ENV/bin/activate

python3 ../returnn/rnn.py ./returnn_tests/tf-neural-transducer.rimes.seq2seq.config


