source $PWD'/opencv/bin/activate'

proto=$PWD'/caffe/deploy.prototxt.txt'
echo $proto

weights=$PWD'/caffe/res10_300x300_ssd_iter_140000.caffemodel'
echo $weights

python UAMS.py -p $proto -w $weights
