import string

def open_and_read(path):
    df = open(path, "r")
    lines = df.read().strip().split('\n')
    return lines


def clean_sent(sent):
  sent = sent.lower()
  cleant = ''
  for i in range(len(sent)):
    if sent[i] not in string.punctuation:
      cleant+=sent[i]
  return cleant


def cleant_sentences(lines):
  english_sentences = []
  french_sentences = []
  for i in range(len(lines)):
    eng, fre, _ = lines[i].split('\t')
    eng = clean_sent(eng)
    fre = clean_sent(fre)
    english_sentences.append(eng)
    french_sentences.append(fre)
  english = english_sentences
  french = french_sentences
  return [english, french]



