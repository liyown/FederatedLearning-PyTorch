import json
import matplotlib.pyplot as plt

# 从JSON文件中加载数据
with open('./result/cifar10_dirichlet_100.json', 'r') as file:
    data = json.load(file)

loss = data['loss']
accuracy = data['accuracy']

# 绘制损失图表
plt.plot(loss, label='Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.legend()
plt.show()

# 绘制准确率图表
plt.plot(accuracy, label='Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training Accuracy')
plt.legend()
plt.show()
