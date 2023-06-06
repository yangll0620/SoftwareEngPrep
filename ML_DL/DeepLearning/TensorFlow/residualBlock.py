import tensorflow as tf

class Residual(tf.keras.Model):
    """ The Residual block of ResNet"""

    def __init__(self, num_channels, use_1x1conv=False, strides=1):
        super().__init__()
        self.conv1 = tf.keras.layers.Conv2D(
            num_channels, kernel_size = 3, padding ='same', strides=strides)
        self.conv2 = tf.keras.layers.Conv2D(
            num_channels, kernel_size = 3, padding= 'same')
        self.conv3 = None

        if use_1x1conv:
            self.conv3 = tf.keras.layers.Conv2D(
                num_channels, kernel_size = 1, strides = strides)
            
        self.bn1 = tf.keras.layers.BatchNormalization()
        self.bn2 = tf.keras.layers.BatchNormalization()


    def call(self, X):
        Y = self.conv1(X)
        Y = self.bn1(Y)
        Y = tf.keras.activations.relu(Y)
        Y = self.conv2(Y)
        Y = self.bn2(Y)
        if self.conv3 is not None:
            X = self.conv3(X)

        Y += X

        return tf.keras.activations.relu(Y)



# ResNet Model

class ResnetBlock(tf.keras.layers.Layer):
    def __init__(self, num_channels, num_residuals, first_block=False, **kwargs):
        super(ResnetBlock, self).__init__(**kwargs)
        self.residual_layers=[]
        for i in range(num_residuals):
            if i == 0 and not first_block:
                self.residual_layers.append(
                    Residual(num_channels, use_1x1conv=True, strides=2)
                )
            else:
                self.residual_layers.append(Residual(num_channels))

    def call(self, X):
        for layer in self.residual_layers:
            X = layer(X)

        return X




def net():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(64, kernel_size=7, strides=2, padding='same'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Activation('relu'),
        tf.keras.layers.MaxPool2D(pool_size=3, strides=2, padding='same'),

        ResnetBlock(64, 2, first_block=True),
        ResnetBlock(128,2),
        ResnetBlock(256, 2),
        ResnetBlock(512, 2),
        tf.keras.layers.Activation('relu'),
        tf.keras.layers.GlobalAvgPool2D(),
        tf.keras.layers.Dense(units=10)])
    

    return model
    


model = net()

X = tf.random.uniform(shape=(1, 224, 224, 1))

### print each layer in ResNet
for layer in model.layers:
    X = layer(X)
    print(layer.__class__.__name__, 'output shape: \t', X.shape)

import pdb
pdb.set_trace()

### load a dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train/255.0, x_test/255.0
x_train = x_train.expand_dims(x_train, axis = 3)
x_test = x_test.expand_dims(x_test, axis = 3)




### Training
model = net()
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy()

model.compile(optimizer='adam',
              loss = loss_fn,
              metrics= ['accuracy'])

model.fit(x_train, y_train, epochs = 5)
