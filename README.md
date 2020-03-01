# UAMS (User Attentivenes Monitoring System)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To identify Persons behavior is one of the most challenging tasks. Behavior contains facial expression, hand gestures, body postures, etc. Out of that, we use facial expression to identify ones behavior. A facial expression contains information that can be utilized for levels of drowsiness. There are numerous facial highlights that can be extricated from the face to interpret the level of drowsiness. These incorporate eye blinks, yawning and head movements. Though, the development of a drowsiness detection system that produces reliable and precise results is a challenging task as it needs accurate and robust algorithms. A wide-ranging of techniques have been tested to detect user drowsiness earlier. The recent growth of deep learning needs that these algorithms be reexamined to evaluate their accuracy in detection of drowsiness. User Attentiveness Monitoring System (UAMS) detects the Users drowsiness based on behavioral measures using deep learning techniques. UAMS analyses each and every person in the crowd and Classify them into Attentive and Non-attentive using OpenCV and Dlib (Histogram of oriented gradients (HOG) and Support Vector Machine (SVM)) algorithm.

## Problem Definition
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The ﬂow of the proposed system is shown in Fig. 1, First UAMS picks video or image as the input ﬁle, resize it into 300x300 resolution and passes to the caﬀe model. Caﬀe model converts it into Blob which is a collection of binary data stored as a single entity and tries to identify face region and store it into face array and passes to the UAMS. UAMS passes this array to the Dlib. Dlib is a general purpose cross-platform software library written in the programming language C++ which contains HOG+ SVM. Using HOG+ SVM Dlib maps 68-face coordinates on extracted faces. With the help of this left and right eye, mouth region is identiﬁed. Using Euclidean distance formula, calculate eye aspect ratio (EAR), mouth aspect ratio (MAR) and passes to the threshold value, if EAR and MAR are more than the threshold value then the User is drowsy i.e. Unattentive.


<p align="center">
  <img width="500" height="500" src="documentation/images/ProblemDef.PNG">
</p>

## Proposed System Architecture
### Step 1 Data Preparation

##### cv2.cvtColor()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are more than 150 color-space conversion methods available in OpenCV. we use RGB to Gray conversion. Since RGB image takes 24 bits (8 x 3) while grayscale image takes only 8 bits to store and we are interested in developing a time-eﬃcient system, therefore after capturing the image (RGB image) it is converted into a grayscale image. The intensity of an image is the average of the three color elements, so the grayscale image that represents the original color image can be converted as
##### cv2.dnn.blobFromImage() 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this step, we use cv2.dnn.blobFromImage() to store the images. a blob is just a potentially collection of images with the same spatial dimensions (i.e., width and height), same depth (number of channels), that have all be preprocessed in the same manner.

blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size, mean, swapRB=True)

### Step 2 Model Definition
When using OpenCVs deep neural network module with Caﬀe models, well need two sets of ﬁles: 
1.The .prototxt ﬁle(s) which deﬁne the model architecture (i.e., the layers themselves) of SSD framework based on ResNet Architecture. 

2.The .caﬀemodel ﬁle which contains the weights for the actual layers Both ﬁles are used to detect faces and these detected faces are store into face array. Extracted Faces are as follows:

### Step 3 Face Array 
Face Array We detect the faces using cv2.dnn.net.forward() which is the class of OpenCV module which gives location coordinates of the face region. These coordinates manipulate with np.array() which is a function of NumPy which stands for Numerical Python, is a library consisting of multidimensional array objects and a collection of routines for processing those faces. np.array() lies these point with the actual image. Then, obtained face array hand over to Dlib for further process.
<p align="center">
  <img width="200" height="200" src="documentation/images/face1.png">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img width="200" height="200" src="documentation/images/face2.png">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img width="200" height="200" src="documentation/images/face3.png">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>

## Dependencies and Technology Stack

UAMS uses a number of open source projects to work properly:

* [OpenCV](https://opencv.org/) - Computer Vision Library for dnn support.
* [DLIB](http://dlib.net/) - For Facial Landmarks detection.
* [imutils](https://pypi.org/project/imutils/) - For other image related Operation.
* [numpy](https://numpy.org/) - For Conversion of images to text data or pixel values.


### Installation

UAMS requires Python 3.6 or heigher to run properly.

Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ NODE_ENV=production node app
```

### Plugins

Dillinger is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |


### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version} .
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

#### Kubernetes + Google Cloud

See [KUBERNETES.md](https://github.com/joemccann/dillinger/blob/master/KUBERNETES.md)


### Todos

 - Write MORE Tests
 - Add Night Mode

License
----

MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
