# Bert classification: Bernie vs Trump

This repository is a first approach to fine-tuning BERT on a classification downstream task, supporting my talk about BERT.

The task is to classify sentences into two classes, according to whether they belong to Donald Trump or Bernie Sanders. We have manually collected sentences from one speech from 2015 for each of the US presidential candidates ([link](https://www.vox.com/2019/6/12/18663217/bernie-sanders-democratic-socialism-speech-transcript) to Bernie Sanders speech; [link](https://www.kansascity.com/news/local/news-columns-blogs/the-buzz/article55604115.html) to Donald Trump speech). We do not belong the rights of the data and it has only been used for educational purposes.

We have used pre-trained BERT models from [HuggingFace](https://huggingface.co/transformers/installation.html), Pytorch and Pytorch Ignite.

## Setting environment up

Make sure virtualenv >= 20.8.30 and Python >= 3.7 are installed in your system. Then, run:

```python
virtualenv bert && source bert/bin/activate
pip install -r requirements.text
```
