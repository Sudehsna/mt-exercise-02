**TASK 1**

Chosen Data:
We first started training the model with the book "Nathan the Wise; a dramatic poem in five acts by Gotthold Ephraim Lessing" but when we generated a sample text, but the sample was almost unintelligible and we thought this was due to some unconventional formatting which wouldn't allow proper preprocessing. Then we also noticed that it was only around 3000 segments which was too short anyways. We then chose another dataset: "Moby Dick; Or, The Whale by Herman Melville". Moby Dick, being a long and better formatted prose novel, provided better training data.

Special Attributes:
Moby Dick contains distinctive linguistic and thematic features, including 19th-century literary English. These stylistic elements may influence our model to generate longer, more descriptive sentences, potentially with hints of marine language patterns.

Sample Generation:
With the default settings the generated sample exhibits a strong stylistic match to Moby Dick, with references to nautical elements (e.g., “sea,” “harpoon,” “prow”) and dramatic tone. The presence of names like “Ahab” suggests the model successfully internalized important tokens. While semantic coherence is for the most part lacking and <unk> tokens remain present.


**TASK 2**

Connection between perplexities:
There is a clear positive correlation between training, validation, and test perplexity across all models. As training perplexity decreases, validation and test perplexities generally follow the same trend, indicating that the models generalize consistently. Among the dropout settings tested, dropout = 0.5 yielded the best performance, achieving the lowest validation and test perplexity. This suggests that a 50% dropout rate performs best under these circumstances providing the right balance between underfitting and overfitting for our dataset and model configuration.


Best and Worst samples:
While the lower-perplexity model produced slightly more structured and thematically consistent text, featuring phrases related to the sea, boats, and characters like Ahab - the output still lacked grammatical correctness and coherence. The overall fluency was poor, and <unk> tokens appeared frequently.

In contrast, the model with the highest perplexity produced more chaotic and fragmented text with even less structure and weaker thematic relevance.In both cases, the outputs did not convincingly resemble natural or fluent language.
Overall ⁠the model with dropout 0.5 generates more coherent, and stylistically appropriate text(e.g., “whale-boat,” “my boat,” “thou” ). In contrast, dropout 0.9 leads to weird phrasing and less intelligible content which reflects its poor generalization.


Repository: