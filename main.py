import data_preprocessing
import apply_padding
import encoder_decoder
import outputs

lines = data_preprocessing.open_and_read("fra.txt")
english_sentences, french_sentences = data_preprocessing.cleant_sentences(lines)

max_words_in_english_sentence, max_words_in_french_sentence = apply_padding.find_max_words(english_sentences, french_sentences)
english_padded_sentences, french_padded_sentences = apply_padding.tokenize_and_pad(english_sentences, french_sentences, max_words_in_english_sentence, max_words_in_french_sentence)
words_in_english_vocab, words_in_french_vocab = apply_padding.tokenize_and_pad(english_sentences, french_sentences, max_words_in_english_sentence, max_words_in_french_sentence, vocab = True)
english_tokenizer, french_tokenizer = apply_padding.tokenize_and_pad(english_sentences, french_sentences, max_words_in_english_sentence, max_words_in_french_sentence, get_tokenizer=True)



enc_dec_model = encoder_decoder.encoder_decoder_model(max_words_in_english_sentence, max_words_in_french_sentence, words_in_english_vocab, words_in_french_vocab)
enc_dec_model.summary()
loaded_model = encoder_decoder.load_encoder_decoder(enc_dec_model)



while True:
    eng_sent = input("Enter English Sentence: ")
    predicted_french_sent_embedding = outputs.get_output(english_tokenizer, max_words_in_english_sentence, loaded_model, eng_sent)
    index_weights = outputs.manual(predicted_french_sent_embedding)
    output_french_sent = outputs.map_ind_to_words(index_weights, french_tokenizer)
    output_french_sent = outputs.cleant_output(output_french_sent)
    print(output_french_sent)


