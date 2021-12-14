import tensorflow as tf
from tensorflow.keras import layers
import tensorflow_docs as tfdocs
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = np.array(pd.read_csv('data.csv'))
for value in data:
    if value[0] == 'STAR':
        value[0] = 0
    elif value[0] == 'GALAXY':
        value[0] = 1
    elif value[0] == 'QSO':
        value[0] = 2
data = data.astype('float32')
train_labels, train_data, test_labels, test_data = data[:8000, :1], data[:8000, 1:], data[8000:, :1], data[8000:, 1:]

N_TRAIN = len(train_labels)
BATCH_SIZE = 500
STEPS_PER_EPOCH = N_TRAIN//BATCH_SIZE


def compile_and_fit(network, max_epochs=10000):
    network.compile(optimizer=tf.keras.optimizers.Adam(tf.keras.optimizers.schedules.InverseTimeDecay(
                                                        0.001,
                                                        decay_steps=STEPS_PER_EPOCH*1000,
                                                        decay_rate=1,
                                                        staircase=False)),
                    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                    metrics=[
                        tf.keras.losses.BinaryCrossentropy(from_logits=True, name='binary_crossentropy'),
                        'accuracy'
                    ])

    return network.fit(
            train_data,
            train_labels,
            steps_per_epoch=STEPS_PER_EPOCH,
            epochs=max_epochs,
            callbacks=[
                tfdocs.modeling.EpochDots(),
                tf.keras.callbacks.EarlyStopping(monitor='val_binary_crossentropy', patience=200),
            ],
            verbose=0)


model = tf.keras.Sequential([
    layers.Dense(15),
    layers.Dense(13, activation='relu'),
    layers.Dense(11, activation='relu'),
    layers.Dense(9, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(6, activation='sigmoid'),
    layers.Dense(3)
])

result = compile_and_fit(model)

plotter = tfdocs.plots.HistoryPlotter(metric='accuracy', smoothing_std=10)
plotter.plot(result)
plt.ylim([0, 1])

# model.evaluate(test_data, test_labels, verbose=2)
