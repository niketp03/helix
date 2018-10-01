import helix.helix as hlx
import tensorflow as tf
import numpy as np

mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

def choose_activation(x):
	if x < 0.1:
		return tf.nn.relu
	elif x < 0.2:
		return tf.nn.relu6
	elif x < 0.3:
		return tf.nn.crelu
	elif x < 0.4:
		return tf.nn.relu
	elif x < 0.5:
		return tf.sigmoid
	elif x < 0.6:
		return tf.tanh
	elif x < 0.7:
		return tf.nn.selu 
	elif x < 0.8:
		return tf.nn.softsign
	elif x < 0.9:
		return tf.nn.softplus
	elif x < 1:
		return tf.nn.elu 

def fitness(dna):
	model = tf.keras.models.Sequential()
	model.add(tf.keras.layers.Flatten())
	model.add(tf.keras.layers.Dense(int(dna[0]*255)+1, activation=choose_activation(dna[2])))
	model.add(tf.keras.layers.Dense(int(dna[1]*255)+1, activation=choose_activation(dna[3])))
	model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
	model.compile(optimizer='adam',
	              loss='sparse_categorical_crossentropy',
	              metrics=['accuracy'])
	model.fit(x_test, y_test, epochs=1)
	val_loss, val_acc = model.evaluate(x_train, y_train)
	print(val_loss)
	print(val_acc)
	return val_loss


darwin = hlx.Genetic(4, 20, children = True, mutation = False, immigrant_factor=0.7)
darwin.evolve(fitness, 20)
