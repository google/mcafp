MC-AFP is a machine comprehension dataset that is generated based on the public
available Gigaword dataset (AFP portion). The technique to create such a dataset
is reported in the paper:

"Building Large Machine Reading-Comprehension Datasets using Paragraph Vectors",
Radu Soricut, Nan Ding.

We generate a datasets of around 2 million examples,
on which we estimate that the human-level accuracy is in the 90% range
(in a 5-way multi-choice setup; for comparison, a random-guess approach has 20%
accuracy).
A novel neural-network architecture that combines the representation power
of recursive neural networks with the discriminative power of fully-connected
multi-layered networks achieves the best results we could obtain on our dataset:
83.2% accuracy.

What is enclosed in this package is an encrypted MC-AFP dataset and the code
which decodes the encrypted dataset.

Datasets needed:
D1. English Gigaword Fifth Edition (LDC2011T07) from the Linguistic
    Data Consortium (LDC).
    [We cannot provide you with this dataset, please contact LDC
    at https://www.ldc.upenn.edu/].
D2. The MC-AFP dataset that comes with this package, see data/

Decoding procedure:
1. Specify the path to "(Dataset D1)" in ${LDCDIR} of generate_text.sh
2. Specify the output directory in ${OUTDIR} of generate_text.sh
3. sh generate_text.sh
4. When finished, the final dataset should be in ${OUTDIR}
