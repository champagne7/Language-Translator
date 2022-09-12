import tensorflow
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences


def find_max_words(english_sentences, french_sentences):
    max_engsent_len = 0
    max_fresent_len = 0
    for i in range(len(english_sentences)):
        english_sentences[i] = english_sentences[i].split()
        max_engsent_len = max(max_engsent_len, len(english_sentences[i]))
    for i in range(len(french_sentences)):
        french_sentences[i] = french_sentences[i].split()
        max_fresent_len = max(max_fresent_len, len(french_sentences[i]))
    return [max_engsent_len, max_fresent_len]


def tokenize_and_pad(english, french, max_engsent_len, max_fresent_len, vocab=False, get_tokenizer=False):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(english)
    tokenizer1 = Tokenizer()
    tokenizer1.fit_on_texts(french)

    eng_text_tokenized = tokenizer.texts_to_sequences(english)
    fre_text_tokenized = tokenizer1.texts_to_sequences(french)
    words_in_english_vocab = len(tokenizer.word_index)+1
    words_in_french_vocab = len(tokenizer1.word_index)+1

    eng_pad_sentences = pad_sequences(eng_text_tokenized, max_engsent_len, padding="post")
    fre_pad_sentences = pad_sequences(fre_text_tokenized, max_fresent_len, padding="post")

    if vocab:
        return [words_in_english_vocab, words_in_french_vocab]
    if get_tokenizer:
        return [tokenizer, tokenizer1]

    return [eng_pad_sentences, fre_pad_sentences]

