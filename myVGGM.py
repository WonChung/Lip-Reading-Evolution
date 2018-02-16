#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:35:34 2018

@author: angelina
"""
import tensorflow as tf
from keras.models import Sequential
from keras.layers import (Dense, Conv2D, Activation, ZeroPadding2D, 
                            MaxPooling2D, Flatten, Dropout)
from keras.layers import Lambda


class VGGM():
    def __init__(self):

    def lrn(input, radius=2, alpha=.001, beta=.75, name='LRN', bias=1.0):
            return tf.nn.local_response_normalization(input,
                                                      depth_radius=radius,
                                                      alpha=alpha,
                                                      beta=beta,
                                                      bias=bias,
                                                      name=name)
    def build_model(self):

        self.model = Sequential(
                [Conv2D(96,7,7, subsample=(2,2),input_shape=imn, trainable=train),
                 Activation('relu'),
                 #LRN
                 Lambda(lrn),
                 MaxPooling2D((3,3),(2,2)),
        
                 Conv2D(256,5,5, subsample=(2,2), trainable=train),
                 Activation('relu'),
                 #LRN
                 Lambda(lrn),
                 MaxPooling2D((2,2)),
                 
                 Conv2D(512,3,3,activation='relu', trainable=train),
                 ZeroPadding2D((1,1)),
                 Conv2D(512,3,3,activation='relu', trainable=train),
                 ZeroPadding2D((1,1)),
                 
                 Conv2D(512,3,3,activation='relu', trainable=train),
                 MaxPooling2D((2,2)),
        
                 Flatten(),
                 Dense(4096, activation='relu', trainable=train),
                 #Dense(4096, activation='relu', trainable=train),
                ]
            )
        
    
    def fit(self):
        pass
    
    def predict(self):
        pass
    
    
    
    
    
    