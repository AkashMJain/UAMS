
source $PWD'/opencv/bin/activate'

proto=$PWD'/caffe/deploy.prototxt.txt'
echo $proto

weights=$PWD'/caffe/res10_300x300_ssd_iter_140000.caffemodel'
echo $weights

video=$PWD'/test_data/test_data2.mov'
echo $video

python UAMS.py -p $proto -w $weights -v $video


# python UAMS.py -p caffe/deploy.prototxt.txt -w caffe/res10_300x300_ssd_iter_140000.caffemodel -v test_data/test_data2.mov
