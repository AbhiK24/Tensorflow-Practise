
from __future__ import print_function

import tensorflow as tf

# Addition and multiplication with constants

a = tf.constant(2)
b = tf.constant(3)


with tf.Session() as sess:
    print("a=2, b=3")
    print("This will Add using constants: %i" % sess.run(a+b))
    print("This will Multiply using constants: %i" % sess.run(a*b))


# Addition and multiplication with variables

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

add = tf.add(a, b)
mul = tf.mul(a, b)

with tf.Session() as sess:
    print("Addition with variables: %i" % sess.run(add, feed_dict={a: 2, b: 3}))
    print("Multiplication with variables: %i" % sess.run(mul, feed_dict={a: 2, b: 3}))




