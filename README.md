# VISUALIZATION_TOOLS_UCLA_SU23



![download](https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/9c5a1cdf-7fbb-43d3-91f4-fa7a512c1a33)

# About
This repository contains code that creates visualizations which aid in the research and treatment for individuals affected by metastatic brain tumors.

# Applications & Organization
All the code for this project is contained within the "UCLA_SU23_Work" folder. There are 3 main folders within UCLA_SU23_Work:

1) "demo"
2) "graphvis"
3) "slicer"

Demo: The demo folder contains a python file, "Codefile.py", in which I modified existing code which launched a 3D interactive brain viewer to include a drop-down menu that contains the options "lung", "breast", "kidney", "melanoma", and "colorectal". When applied to real-world patient data, this drop down menu would allow users to see how these different types of cancers have metastisized in patient's brains. For example, when a user clicks on "lung", the 3D brain that appears in the interactive viewer will display areas in the brain affected by tumors for lung cancer patients only. The image below displays the brain viewer when "lung" is selected using randomized data. However, when real-patient data is fed in, the deliniations between the tumorous and non-tumorous regions should become more clear.


<img width="960" alt="demo_image_1" src="https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/a0ba15a5-36d0-42c0-947a-9eaeff2a8a3e">

Lastly, the original code I modified can be found at this link: 
https://gallantlab.org/pycortex/auto_examples/webgl/multiple_datasets.html#sphx-glr-auto-examples-webgl-multiple-datasets-py


Graphvis: The graphvis folder contains an initializer file, "init.py" and the main code file, "app.py". This file contains code that launches an interactive x-y axis and linear graph. When combined with the patient data used in the  which can later be utilized to graph relationships between brain volume and tumor types using data from the 3D interactive brain viewer.


The slicer folder contains an "assets" folder, a "brain_images" folder, and a "MNIST_data" folder. It also contains 5 code files - the initializer file ("init.py"), "main.py", "main2.py", "main3.py", and "MNIST_images.ipynb." In main.py, I used existing code that launches an interactive 3D animation of slices of a brain scan but I modified the code to run using Dash. The brain image in the animation is contained in the "attention-mri.tif" file in the assets folder. Main2.py launches the same animation as main.py except it incorporates tooltip to show different images in the hover textbox of the brain animation based on the x-value the user is currently hovering on. Specifically, if the user is hovering on x-values [0:50], it displays "Image1.jpg". If the user is hovering on x-values [51:100], it displays "Image2.jpg". Lastly, if the user is hovering on x-values 101 or greater, it displays "Image3.jpg". These 3 images can be found in the "brain_images" folder. Lastly, main3.py is similar to main2.py but it displays a different image for every possible x-value a user can hover over (values 0-155). These images are saved in the "MNIST_data" folder which were drawn from the "mini-mnist-1000.pickle" file and converted to jpeg using code found in the "MNIST_images.ipynb" file. These animations can be utilized to view certain brain scans based on a specific location in the brain.

How to run the code: In order to run the different code files, first, Docker Desktop must be running since all the code runs using Docker. Then, there are 4 main files involved in running the code - "Dockerfile.demo", "Dockerfile.graphvis", "Dockerfile.slicer", and "run.sh". "Dockerfile.demo" contains the docker script to run "Codefile.py". "Dockerfile.graphvis" contains the docker script to run "app.py". "Dockerfile.slicer" contains the docker script to run either "main.py", "main2.py", or "main3.py". Lastly, "run.sh" contains the bash script to build and run any of the docker files. In order to actually launch the visualizations, open a new bash terminal and type either "bash run.sh demo", "bash run.sh graphvis", or "bash run.sh slicer" depepending on which visualization you want to launch. Finally, to view the visualization, you will have to access the port that was opened specified in the bash terminal. Please note: In order to run "Codefile.py", after running "bash run.sh demo", Ipython will be launched in the terminal and the code contained in "Codefile.py" must be pasted into Ipython and then the visualization will be viewable on the port. In order to run "main.py", "main2.py", or "main3.py", the name of the file you want to run must be updated accordingly in the "Dockerfile.slicer" file in the locations where it says "main_" (3 locations total). The port numbers for the different visualizations can also be updated by changing the port number in the corresponding section in "run.sh" and the corresponding docker file.

