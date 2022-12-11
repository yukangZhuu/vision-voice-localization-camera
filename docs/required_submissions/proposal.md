# Project Proposal

## 1. Motivation & Objective

The project objective is to develop a vision and voice fusion camera which can detect and tell which person is talking in a camera frame. The motivation of the project originates from the multi-person scenario of speech recognition. To realize the multi-person speech recognition, it's important to deciede which of the visible faces corresponds to the voice at each moment. More details will be illustrated in the next section.

## 2. State of the Art & Its Limitations

As an important sub-branch of speech recognition, audio-visual automatic speech recognition (A/V ASR) [1] [2] has been studied a lot recently to deal with the scenario where multiple people are simultaneously on the screen. In addition to the voice signal that is necessary for traditional speech recognition, A/V ASR takes great benefits from the addition of visual signal contained in a video where the speakers’ faces show. To achieve high performance in speech recognition with a visual scene of more than one speaker, A/V ASR also requires solving the active speaker detection (ASD) problem, which means deciding which of the visible faces relates to the voice at each moment [3]. Traditional ASD requires short-term or long-term audio and visual information to accurately extract features of different speakers [4], which may require complex modeling and time-costing training to achieve satisfactory performance in a real-time scenario.

## 3. Novelty & Rationale

To simplify this active speaker detection problem, Our project proposes to substitute ASD by changing the problem-solving time and stage: instead of conducting ASD to a completely recorded video, we can solve the “which person” dilemma at the very moment when the video is been recorded by a camera. In particular, by combining human detection and sound source localization (SSL) in real-time, we can achieve ASD in a camera frame without complicated audio-visual feature extraction. Specifically, we aim to develop a vision & voice localization camera to leverage the fusion of human detection and voice directioning in real-time, so that it is able to highlight the person that is giving voice, realizing a pre-stage active speaker detection.

## 4. Potential Impact

As described in the last section, active speaker detection (ASD) problem is a key constraints in realizing audio-visual automatic speech recognition (A/V ASR). If we ca n achieve a pre-stage active speaker detection with good performance, the complexity of active speaker detection can be greatly alleviated, thus changing the mechanism and algorithm structure of A/V ASR.

## 5. Challenges

The challenge of the vision & voice localization camera originates in two main technical approaches mentioned above: human detection and sound source localization. For human detection, we introduced the popular vision AI YOLOv5, which is a family of well-trained compound-scaled object detection models. For SSL, we leveraged a 4-microphone array module named Respeaker to realize the required algorithms. 

## 6. Requirements for Success

As described above, the basic requirements for this projects lie in the two main technical approaches: human detection and sound source localization. The realization of this two functions are the most important prequsite. Specifically, for human detection, we need high accuracy and low latency to correctly detect human in camera frame. So a mature object detection model is needed. For sound source localization, accuracy is still important, so it's better to use a existing hardware module such as microphone array product rather than building the sound processing hardware ourselves.  

## 7. Metrics of Success

A key assessment for our project is the performance in the multi-person scenario. Whether the device can give a continuously stable stream of active speaker detection results is the main concern of this project. Correspondingly, we also plan to develop a mechanism to deal with the multi-sound-source scenario. Furthermore, aliasing and latency are also considered important metrics for the vision & voice localization camera. To correctly conduct active speaker detection, the SSL of the device should have a relatively low minimum angular separation to maintain good discernibility and avoid detection aliasing.

## 8. Execution Plan

As described above, there are mainly two technical tasks in this project, which are human detection and sound source localization. These two parts will be developed simutaneously. For human detection, we plan to do it on PC with a YOLOv5 model. For SSL part, we plan to use the Respeaker mic-array and a Raspberry Pi. For work partition, Hanyi Duan will be responsible for the human detection part of the vision & voice localization camera and Yukang Zhu will work on the sound source localization part of the project as well as the central controlling logic.

## 9. Related Work

### 9.a. Papers

For now, two papers are considered. One for human detection and one for sound source localization.

Human Detection:
YOLOv4: Optimal Speed and Accuracy of Object Detection [5]
https://arxiv.org/abs/2004.10934


Sound Source Localization:
Sound localization based on acoustic source using multiple microphone array in an indoor environment [6]
https://www.mdpi.com/2079-9292/11/6/890


### 9.b. Datasets

Human Detection: The weights of yolov5.pt are used, which is trained with MS COCO dataset.

### 9.c. Software

We will use Python, Anaconda for virtual environments, Raspberry Pi OS, and YOLOv5.

## 10. References

[1] O. Braga and O. Siohan, “A Closer Look at Audio-Visual Multi-Person Speech Recognition and Active Speaker Selection,” ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2021, pp. 6863-6867, doi: 10.1109/ICASSP39728.2021.9414160.

[2] T. Afouras, J. S. Chung, A. Senior, O. Vinyals and A. Zisserman, “Deep Audio-Visual Speech Recognition,” in IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 44, no. 12, pp. 8717-8727, 1 Dec. 2022, doi: 10.1109/TPAMI.2018.2889052.

[3] O. Braga, T. Makino, O. Siohan and H. Liao, “End-to-End Multi-Person Audio/Visual Automatic Speech Recognition,” ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2020, pp. 6994-6998, doi: 10.1109/ICASSP40776.2020.9053974.

[4] Ruijie Tao, Zexu Pan, Rohan Kumar Das, Xinyuan Qian, Mike Zheng Shou, and Haizhou Li. 2021. Is Someone Speaking? Exploring Long-term Temporal Features for Audio-visual Active Speaker Detection. In Proceedings of the 29th ACM International Conference on Multimedia (MM ‘21). Association for Computing Machinery, New York, NY, USA, 3927–3935.

[5] Bochkovskiy, A., Wang, C., & Liao, H.M. (2020). YOLOv4: Optimal Speed and Accuracy of Object Detection. arXiv:2004.10934v1 [cs.CV].

[6] Chung, M., Chou, H., & Lin, C. (2022). Sound localization based on acoustic source using multiple microphone array in an indoor environment. Electronics, 11(6), 890. doi:10.3390/electronics11060890
