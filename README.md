# Rice-Leaf-Diseases-Detection-And-Classification
<img src="https://image.freepik.com/free-photo/rice-blast-disease-rice-diseases-damage-rice-grains-paddy-farms_46178-489.jpg" alt="tomato" width="1000" height="510">
<p>Rice is an inseparable part of Indian's diet, and that's why India every year produces a whopping 104.80 million tonnes of rice. Rice is counted as one of the most labor-intensive crops to grow, rice crops often suffer from soil moisture stress due to erratic, inadequate rainfall, and other enviromental factors. This mostly results as forming and spread of diseases which highly damages the crop fields and cause wastage of money and time to farmers. To battle against this problem and proved farmers a cheaper and faster means of understanding the crop diseases, I have created a deep learning model that is <b>capable of identifying 5 rice diseases with an accuracy of 92%.</b></p> 
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
<p>The deep learning model at its core uses four convolutional neural network layers followed by Max pooling layers for recognizing the rice diseases, it also uses three dense layers for decision making. All the layers use RELU as an activation function except the last dense layer that uses the softmax activation function. During training, the model uses Adam as an optimizer for performing backpropagation and uses categorical cross-entropy as the loss function. </p>
<h2>Model Training</h2>
<ul>
  <li><h3>Loss<h3></li>
</ul>
<img src="https://github.com/NavinBondade/Rice-Leaf-Diseases-Detection-And-Classification/blob/main/Rice%20Diseases%20Classification%20and%20Prediction/Graph/loss.png" width="450" height="300">
<ul>
  <li><h3>Accuracy<h3></li>
</ul>
<img src="https://github.com/NavinBondade/Rice-Leaf-Diseases-Detection-And-Classification/blob/main/Rice%20Diseases%20Classification%20and%20Prediction/Graph/accuracy.png" width="450" height="300">
