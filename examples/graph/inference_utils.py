import os
import numpy as np
import math
import scipy
import sys


def inference_via_confidence(confidence_mtx1, confidence_mtx2, label_vec1, label_vec2):
	# ----------------First step: obtain confidence lists for both training dataset and test dataset--------------
	confidence1 = []
	confidence2 = []
	acc1 = 0
	acc2 = 0
	for num in range(confidence_mtx1.shape[0]):
		confidence1.append(confidence_mtx1[num, label_vec1[num]])  # 添加的是真实label的概率
		#confidence1.append(np.argmax(confidence_mtx1[num, :]))
		if np.argmax(confidence_mtx1[num, :]) == label_vec1[num]:  # 如果最大的概率就是真实的label，acc1+1
			acc1 += 1

	for num in range(confidence_mtx2.shape[0]):
		confidence2.append(confidence_mtx2[num, label_vec2[num]])
		#confidence2.append(np.argmax(confidence_mtx2[num, :]))
		if np.argmax(confidence_mtx2[num, :]) == label_vec2[num]:
			acc2 += 1
	confidence1 = np.array(confidence1)  #训练集中真实标签的概率
	confidence2 = np.array(confidence2)  #测试集中真实标签的概率

	print('model accuracy for training and test-', (acc1 / confidence_mtx1.shape[0], acc2 / confidence_mtx2.shape[0]))

	# sort_confidence = np.sort(confidence1)
	sort_confidence = np.sort(np.concatenate((confidence1, confidence2))) #所有节点的真实标签的概率
	max_accuracy = 0.5
	best_precision = 0.5
	best_recall = 0.5
	for num in range(len(sort_confidence)):
		delta = sort_confidence[num]
		ratio1 = np.sum(confidence1 >= delta) / confidence_mtx1.shape[0] #训练集中大于这个阈值的所有节点所占的比例
		ratio2 = np.sum(confidence2 >= delta) / confidence_mtx2.shape[0] #测试集中大于这个阈值的所有节点所占的比例
		accuracy_now = 0.5 * (ratio1 + 1 - ratio2)
		if accuracy_now > max_accuracy:
			max_accuracy = accuracy_now
			best_precision = ratio1 / (ratio1 + ratio2)
			best_recall = ratio1
	print('membership inference accuracy is:', max_accuracy)
	return max_accuracy