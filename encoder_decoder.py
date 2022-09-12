from keras.layers import LSTM, Input, TimeDistributed, Dense, Activation, RepeatVector, Embedding, Bidirectional
from keras.models import Model
from keras.optimizers import Adam
from keras.losses import sparse_categorical_crossentropy
import os
import tensorflow

def encoder_decoder_model(max_engsent_len, max_fresent_len, words_in_english_vocab, words_in_french_vocab):
    input_sequence = Input(shape=(max_engsent_len, ))
    embedding = Embedding(input_dim=words_in_english_vocab, output_dim=128,)(input_sequence)
    encoder = Bidirectional(LSTM(64, return_sequences=False))(embedding)
    r_vec = RepeatVector(max_fresent_len)(encoder)
    decoder = LSTM(64, return_sequences=True, dropout=0.2)(r_vec) 
    logits = TimeDistributed(Dense(words_in_french_vocab))(decoder)

    enc_dec_model = Model(input_sequence, Activation('softmax')(logits))
    enc_dec_model.compile(loss=sparse_categorical_crossentropy,
                optimizer=Adam(1e-3),
                metrics=['accuracy'])
    # enc_dec_model.summary()
    return enc_dec_model

def load_encoder_decoder(enc_dec_model):
    checkpoint_path = "training_1/cp.ckpt"
    # checkpoint_dir = os.path.dirname(checkpoint_path)
    # cp_callback = tensorflow.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path, save_weights_only=True, verbose=1)
    # model_results = enc_dec_model.fit(eng_pad_sentences, fre_pad_sentences, batch_size=30, epochs=100, callbacks=[cp_callback])
    enc_dec_model.load_weights(checkpoint_path)
    return enc_dec_model



