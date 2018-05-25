# abnormal_4classify
codes for abnormal classify 
------
Description
========
    It's a demonstration project,by detecting  image from web video camera . Before the image enters the neural network,
    I do some image_processing , by detecting multiple ROI windows' value to find out abnormal area. Due to background 
    interference is too heavy ,I use double threshold check to insure image which sended into ML is abnormal.
Dependencies
=====
    PyQt4
    numpy
    opencv(build with ffmpeg)
    matplotlib
    
    relation:
    -----
      This is client,  ML is related to 8 layers Neural Networks.
  
