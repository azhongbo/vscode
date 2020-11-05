#!/usr/bin/python3
import sys
from __save__ import *

########################################################
def runAllData(MyCodeTitle,MyCodeString,MyCodeName):
    global package1,package2,extension,count

    count = count + 1    

    (data1,data2,data3) = makeCode(MyCodeTitle,MyCodeString,MyCodeName+str(count))

    package1  = package1  + data1
    package2  = package2  + data2
    extension = extension + data3
########################################################


package1   = ""
package2   = ""
extension  = ""
count      = 0
MyCodeName = sys.argv[2]


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode tf2 Basic ( xxxx )"
# MyCodeString = '''
# ###  Tensorflow2 xxxx ####
# ### file: mainCode_tf2_basic
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode tf2 Basic ( xxxx )"
# MyCodeString = '''
# ###  Tensorflow2 xxxx ####
# ### file: mainCode_tf2_basic
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode tf2 Basic ( xxxx )"
# MyCodeString = '''
# ###  Tensorflow2 xxxx ####
# ### file: mainCode_tf2_basic
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode tf2 Basic ( plt 顯示 mnist / car10 / cifar100 圖片 )"
MyCodeString = '''
###  Tensorflow2 xxxx ####
### file: mainCode_tf2_basic
import matplotlib.pyplot as plt
import numpy as np
def myShow(x_data, y_data ):
    plt.figure(figsize=(5, 3))
    plt.subplots_adjust(hspace=0.1)
    for n in range(15):
        plt.subplot(3, 5, n+1)
        plt.imshow(x_data[n])
        plt.axis('off')
    print(y_data[:15])

(x1,y1), (x1_,y1_) = datasets.mnist.load_data()
(x2,y2), (x2_,y2_) = datasets.cifar10.load_data()
(x3,y3), (x3_,y3_) = datasets.cifar100.load_data()

myShow(x1,y1)
# myShow(x2,np.reshape(y2,[-1]))
# myShow(x3,np.reshape(y3,[-1]))
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode tf2 Basic ( gpu cuda memory error  )"
MyCodeString = '''
### file: mainCode_tf2_basic

import  os
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ['CUDA_VISIBLE_DEVICES'] = "0"  # 選擇GPU
config = ConfigProto()
config.allow_soft_placement=True  #指定設備不存在，允许TF自動分配設備
config.gpu_options.per_process_gpu_memory_fraction=0.8  # 分配 memory 避免溢出
config.gpu_options.allow_growth = True   # 自動分配 GPU RAM
session = InteractiveSession(config=config)

## 處理 cudnn error
## FROM https://davistseng.blogspot.com/2019/11/tensorflow-2.html
def solve_cudnn_error():
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            # Currently, memory growth needs to be the same across GPUs
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            logical_gpus = tf.config.experimental.list_logical_devices('GPU')
            print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
        except RuntimeError as e:
            # Memory growth must be set before GPUs have been initialized
            print(e)
solve_cudnn_error()
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode tf2 Basic ( cpu gpu test )"
MyCodeString = '''
###  Tensorflow2 cpu gpu test ####
### file: mainCode_tf2_basic

import tensorflow as tf
import timeit

with tf.device('/cpu:0'):
    cpu_a = tf.random.normal([10000, 1000])
    cpu_b = tf.random.normal([1000, 2000])
    print(cpu_a.device, cpu_b.device)

with tf.device('/gpu:0'):
    gpu_a = tf.random.normal([10000, 1000])
    gpu_b = tf.random.normal([1000, 2000])
    print(gpu_a.device, gpu_b.device)

def cpu_run():
    with tf.device('/cpu:0'):
        a = tf.matmul(cpu_a, cpu_b)
    return a

def gpu_run():
    with tf.device('/gpu:0'):
        a = tf.matmul(gpu_a, gpu_b)
    return a


cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=10)
print('Run1: ', cpu_time, gpu_time , cpu_time/gpu_time )

cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=10)
print('Run1: ', cpu_time, gpu_time , cpu_time/gpu_time )

cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=10)
print('Run1: ', cpu_time, gpu_time , cpu_time/gpu_time )
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode tf2 Basic ( mnist )"
MyCodeString = '''
###  Tensorflow2 mnist ####
### file: mainCode_tf2_basic
import  tensorflow as tf
from    tensorflow.keras import datasets, layers, optimizers, Sequential, metrics

(xs, ys),_ = datasets.mnist.load_data()

xs = tf.convert_to_tensor(xs, dtype=tf.float32) / 255.
db = tf.data.Dataset.from_tensor_slices((xs,ys)).batch(200)

model = Sequential([ layers.Dense(512, activation='relu'),
                     layers.Dense(256, activation='relu'),
                     layers.Dense(10) ])

model.build(input_shape=(None, 28*28))
model.summary()

optimizer = optimizers.SGD(lr=0.001)
acc_meter = metrics.Accuracy()

def train_epoch(epoch):

    for step, (x,y) in enumerate(db):

        with tf.GradientTape() as tape:        
            x        = tf.reshape(x, (-1, 28*28))   # x        [?, 28, 28] => [?, 784]        
            y_onehot = tf.one_hot(y, depth=10)      # y_onehot [?]         => [?, 10]        
            out = model(x)                          # out      [?, 784]    => [?, 10]                
            loss = tf.square(out-y_onehot)          # loss     [?, 10]        
            loss = tf.reduce_sum(loss) / x.shape[0] # loss     [?]

        acc_meter.update_state(tf.argmax(out, axis=1), y)

        grads = tape.gradient(loss, model.trainable_variables)  ## 優化 和 更新 [w1,w2,w3,b1,b2,b3]
        optimizer.apply_gradients(zip(grads, model.trainable_variables)) ## w' w-lr*grad


        if step % 200==0:

            print(step, 'loss:', float(loss), 'acc:', acc_meter.result().numpy())
            acc_meter.reset_states()


for epoch in range(30):
    train_epoch(epoch)

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode tf2 Basic ( linear_regression )"
MyCodeString = '''
###  Tensorflow2 linear_regression ####
### file: mainCode_tf2_basic
#https://github.com/aymericdamien/TensorFlow-Examples/blob/master/tensorflow_v2/notebooks/2_BasicModels/linear_regression.ipynb
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Training Data.
X = np.array([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1])
Y = np.array([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3])

W = tf.Variable(np.random.randn(), name="weight")
b = tf.Variable(np.random.randn(), name="bias")

# Optimization process. 
def run_optimization(step):
    # Wrap computation inside a GradientTape for automatic differentiation.
    with tf.GradientTape() as g:
        pred = ( W * X + b )  # Linear regression (Wx + b).
        loss= tf.reduce_mean(tf.square( pred - Y)) # Mean square error.
        
        if step % 50 == 0:
            print( f"step: {step}, loss: {loss}, W: {W.numpy()}, b: {b.numpy()}" )
            #print("step: %i, loss: %f, W: %f, b: %f" % (step, loss, W.numpy(), b.numpy()))

    # Compute gradients.
    gradients = g.gradient(loss, [W, b])
    
    # Stochastic Gradient Descent Optimizer.
    # Update W and b following gradients.
    #optimizer.apply_gradients(zip(gradients, [W, b]))
    tf.optimizers.SGD(0.01).apply_gradients(zip(gradients, [W, b]))

# Run training for the given number of steps.
training_steps = 1000

for step in range(1, training_steps + 1):
    # Run the optimization to update W and b values.
    run_optimization(step)
        
# Graphic display
plt.plot(X, Y, 'ro', label='Original data')
plt.plot(X, np.array(W * X + b), label='Fitted line')
plt.legend()
plt.show()
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)

### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode tf2 Basic ( fashion mnist 圖像分類 )"
MyCodeString = '''
###  Tensorflow2 fashion mnist 圖像分類 ####
### file: mainCode_tf2_basic
# TensorFlow and tf.keras
# https://www.tensorflow.org/tutorials/keras/classification
# https://geektutu.com/post/tf2doc-ml-basic-image.html

import tensorflow as tf
from tensorflow import keras
import numpy as np

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)

# 使用 predict函數進行預測
predictions = model.predict(test_images)
predictions[0]
np.argmax(predictions[0]) # 9
test_labels[0] # 9
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)






##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
