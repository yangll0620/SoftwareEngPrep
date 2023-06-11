## Inside TensorFlow: tf.Keras

Note from youtube video https://www.youtube.com/watch?v=UYRBHFAvLSs

### The Keras architecture
- Engine
    - Base Layer
    - Base Network(internal): DAG of Layers
    - Model (training.py): Network + training/eval loops
    - Sequential
- Layers
    - Various subclasses of Layer
- Losses, Metrics
    - Base Metrics
    - Base Loss
    - Various subclasses of Metrics & Loss
- Callbacks
    - Base Callback
    - Various subclasses of Callback
- Optimizers
    - Base Optimizer
    - Various subclasses of Optimizer
- Regularizers, Constraints


### Model vs Layer in tf.Keras
- Model does everything a Layer does +
    - Training (.compile(), .fit(), evaluate(), .predict())
    - Saving(.save()- includes configuration (topology), state(weights), optimizer)
    - Summary/ model visulization (.summary(), plot_model())


- Layer == what we refer to in the literature as a "layer" (as in "convolution layer" or "recurrent layer") or as a "block" (as in "ResNet block" or "Inception block")

- Model == what we refer to in the literature as a "model" (as in "deep learning model") or as a "model" (as in "deep neural network")

- Use the Layer class to define the inner computation blocks, use the Model class to define the outer model

- Example: ResNet50 model: several ResNet blocks subclassing Layer + end-to-end ResNet Model
