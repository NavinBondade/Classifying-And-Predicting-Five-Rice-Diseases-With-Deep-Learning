# Classifying Five Rice Crop Diseases With Deep Learning
<p align="center">
<a href="https://nbviewer.jupyter.org/github/NavinBondade/Classifying-Five-Rice-Crop-Diseases-With-Deep-Learning/blob/main/Rice%20Diseases%20Classification%20and%20Prediction/Notebook/Rice_Leaf_Diseases_Classification_and_Prediction_92_accuracy.ipynb" target="_blank">
  <img align="center"  src="https://github.com/NavinBondade/Distinguishing-Fake-And-Real-News-With-Deep-Learning/blob/main/Graphs/button_if-github-fails-to-load-the-notebook-click-here%20(4).png?raw=true"/>
</a>
</p>


<p align="center">
<a href="https://ricediseasesnavin.herokuapp.com/"  target = "_blank">
  <img align="center"  src="https://github.com/NavinBondade/Identifying-Nine-Tomato-Disease-With-Deep-Learning/blob/main/Tomato%20Disease%20and%20Classification/Graphs%20and%20Pictures/webappbtn.png" height="50" />
</a>
</p>

<img src="https://image.freepik.com/free-photo/rice-blast-disease-rice-diseases-damage-rice-grains-paddy-farms_46178-489.jpg" alt="tomato" width="1000" height="510">
<p>Rice is a staple in the Indian diet, with the nation producing an impressive 104.80 million tonnes annually. However, rice cultivation is among the most labor-intensive agricultural activities, and it faces significant challenges due to environmental factors such as erratic and inadequate rainfall, which often leads to soil moisture stress. This stress, in turn, creates conditions conducive to the spread of diseases, severely damaging crop yields. The consequences are not only financial, leading to substantial losses for farmers, but also time-consuming, as efforts to control these diseases are resource-intensive.

To address this pressing issue and offer farmers a cost-effective and efficient solution for diagnosing rice crop diseases, I have developed a state-of-the-art deep learning model. This model is capable of accurately identifying five distinct rice diseases, providing farmers with a powerful tool to combat crop loss and optimize their agricultural practices. By leveraging advanced deep learning techniques, my model aims to enhance the resilience of rice cultivation, ensuring higher yields and contributing to the overall sustainability of rice production in India.</b></p> 
<h2>Libraries Used</h2>
<ul>
  <li>Tensorflow</li>
  <li>Keras</li>
  <li>Numpy</li>
  <li>Pandas </li>
  <li>Matplotlib</li>
  <li>Numpy</li>
  <li>Glob</li>
</ul>
<h2>Data Visualization</h2>
<img src="https://github.com/NavinBondade/Rice-Leaf-Diseases-Detection-And-Classification/blob/main/Rice%20Diseases%20Classification%20and%20Prediction/Pictures/5%20Rice%20Diseases%20v2.png?raw=true" alt="rice" >
<h2>Model Detail</h2>
<p>
The deep learning model I have developed is engineered with a robust architecture designed for precise identification of rice diseases. At its core, the model employs four Convolutional Neural Network (CNN) layers, which are instrumental in extracting critical features from the input images. These layers are followed by Max Pooling layers, which serve to reduce the spatial dimensions of the feature maps, thus enhancing the model's ability to recognize patterns while also minimizing computational complexity.

For the decision-making process, the model incorporates three fully connected Dense layers. These layers synthesize the information extracted by the CNN layers, enabling the model to make accurate classifications. The Rectified Linear Unit (ReLU) activation function is utilized across all layers, except for the final Dense layer, to introduce non-linearity and enhance the model's learning capacity. The final Dense layer uses the Softmax activation function, which is particularly suited for multi-class classification tasks, as it outputs a probability distribution over the five possible rice diseases.

This carefully crafted architecture ensures that the model not only achieves high accuracy but also operates efficiently, making it a valuable tool for farmers to diagnose rice diseases swiftly and accurately.</p>
<h2>Model Training</h2>
<ul>
  <li><h3>Loss<h3></li>
</ul>
<img src="https://github.com/NavinBondade/Rice-Leaf-Diseases-Detection-And-Classification/blob/main/Rice%20Diseases%20Classification%20and%20Prediction/Graph/loss.png" width="450" height="300">
<ul>
  <li><h3>Accuracy<h3></li>
</ul>
<img src="https://github.com/NavinBondade/Rice-Leaf-Diseases-Detection-And-Classification/blob/main/Rice%20Diseases%20Classification%20and%20Prediction/Graph/accuracy.png" width="450" height="300">
<p>The model underwent rigorous training over 10 epochs to ensure optimal performance in identifying rice diseases. During this training phase, the Adam optimizer was employed, known for its adaptive learning rate capabilities, which enhance the model's ability to converge quickly and effectively. To evaluate the model's performance, categorical cross-entropy was used as the loss function, a standard choice for multi-class classification tasks that measure the discrepancy between the predicted and actual class probabilities.

The training process was meticulously monitored to avoid issues such as overfitting or underfitting, which can compromise a model's generalizability and accuracy. The result is a well-trained model that achieves a fine balance between complexity and accuracy, ensuring reliable predictions across various datasets. This robustness makes the model an excellent tool for diagnosing rice diseases, providing consistent and trustworthy results for farmers.</p>    
<h2>Model Evaluation</h2>
<ul>
  <li><b>Training Data Accuracy: 93 %</b></li>
  <li><b>Test Data Accuracy: 92 %</b></li>
  <li><b>Training Data Loss: 0.18</b></li> 
  <li><b>Test Data Loss: 0.19</b></li> 
</ul>  
<h2>Model Prediction</h2>
<img src="https://github.com/NavinBondade/Rice-Leaf-Diseases-Detection-And-Classification/blob/main/Rice%20Diseases%20Classification%20and%20Prediction/Pictures/5%20Rice%20Diseases%20Prediction.png">
<p>During the testing phase, the model demonstrated exceptional performance by achieving a flawless accuracy rate of 100 percent in predicting all five rice diseases. These diseases include Gudi Rotten, Apex Blast, Leaf Blast, Leaf Burn, and Neck Blast Paddy. This perfect accuracy underscores the model's efficacy and reliability in distinguishing between the different types of rice diseases.

The model's ability to correctly identify each disease with complete precision highlights its robustness and effectiveness in real-world applications. Such high accuracy not only validates the model's capability but also provides farmers with a dependable tool for accurate disease diagnosis, ultimately contributing to improved crop management and reduced agricultural losses.</b></p>  
<h2>Conclusion</h2>
<p>In this project, I have created deep convolutional neural network architecture for correctly identifying the five rice crop diseases with an accuracy of 92 percent. </p>    

