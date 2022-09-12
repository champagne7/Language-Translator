from keras_preprocessing.sequence import pad_sequences


def get_output(tokenizer, max_engsent_len, enc_dec_model, sent):
  tokenized_sent = tokenizer.texts_to_sequences([sent.split()])
  padded_sent = pad_sequences(tokenized_sent, max_engsent_len, padding="post")
  french_sent = enc_dec_model.predict(padded_sent)
  return french_sent

def manual(logits):
    idxs = []
    for i in range(len(logits)):
      for j in range(len(logits[i])):
        maxi = 0
        ind = 0
        for k in range(len(logits[i][j])):
          if logits[i][j][k]>maxi:
            maxi = logits[i][j][k]
            ind = k
        idxs.append(ind)
    return idxs


def map_ind_to_words(idxs, tokenizer1):
    index_to_words = {idx: word for word, idx in tokenizer1.word_index.items()}
    index_to_words[0] = '<empty>'
    return ' '.join([index_to_words[prediction] for prediction in idxs])


def cleant_output(sent):
    cleant = ""
    for i in range(len(sent)):
        if sent[i]=="<":
            break
        cleant+=sent[i]
    return cleant