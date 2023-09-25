# BRAIN_TUMOR_VISUALIZATION_TOOLS



![download](https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/9c5a1cdf-7fbb-43d3-91f4-fa7a512c1a33)

# About
This repository contains code that creates visualizations which aid in the research and treatment for individuals affected by metastatic brain tumors.

# Applications & Code Organization
All the code for this project is contained within the "UCLA_SU23_Work" folder. There are 3 main folders within UCLA_SU23_Work:

1) "Demo"
2) "Graphvis"
3) "Slicer"

#### Demo: #### 
The demo folder contains a python file, "Codefile.py", in which I modified existing code that launched a 3D interactive brain viewer to include a drop-down menu that contains the options "Lung", "Breast", "Kidney", "Melanoma", and "Colorectal". When applied to real-world patient data, this drop down menu would allow users to see how these different types of cancers have metastasized in patient's brains. For example, when a user clicks on "lung", the 3D brain that appears in the interactive viewer will display areas in the brain affected by tumors for lung cancer patients only. In order to interact with the visualization, a user can click on the brain and move it around with their mouse to see different areas of it. The image below displays the brain viewer when "lung" is selected using randomized data. However, when real-patient data is fed in, the delineations between the tumorous and non-tumorous regions should become more clear.

Expected output if "demo" is ran correctly: 
<img width="960" alt="demo_image_1" src="https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/a0ba15a5-36d0-42c0-947a-9eaeff2a8a3e">

Lastly, the original code I modified can be found at this link: 
https://gallantlab.org/pycortex/auto_examples/webgl/multiple_datasets.html#sphx-glr-auto-examples-webgl-multiple-datasets-py


#### Graphvis: #### 
The graphvis folder contains an initializer file, "init.py" and the main code file, "app.py". This file contains code that launches an interactive x-y axis and linear graph. When combined with the "demo" tool and patient data, this graphing framework can be utilized to graph various relationships involving tumor type and tumor location. For example, a user can click on a specific location in the "demo" 3D viewer and can manipulate the graphing tool to graph a desired relationship. These two features are shown below:

Selecting a specific location in "demo":
<img width="960" alt="demo_image_2" src="https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/7f1acf33-58b8-4b6e-b3bd-01c861ec62f2">










Expected output if "graphvis" is ran correctly:
<img width="960" alt="graphvis_image_1" src="https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/024eb407-bd8d-4807-815f-907af3d7edcb">


#### Slicer: #### 
The slicer folder contains an "assets" folder, a "brain_images" folder, and a "MNIST_data" folder. It also contains 5 code files - the initializer file ("init.py"), "main.py", "main2.py", "main3.py", and "MNIST_images.ipynb." 
- In main.py, I used existing code that launched an interactive 3D animation of slices of a brain scan but I modified the code to run using Dash. The pause/play buttons can be used to view different layers of the brain scan and the x, y, z coordinates specify the location in the brain scan the user is hovering over. The brain image used in the animation is contained in the "attention-mri.tif" file in the "assets" folder.

  Expected output if "main" is ran correctly:


<img width="370" alt="main_image1" src="https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/97ac6101-a70a-4aaa-af96-c1e8f8d013e1">

  
- Main2.py launches the same animation as main.py except it incorporates a tooltip to show different images in the hover textbox of the brain animation based on the x-value the user is currently hovering on. Specifically, if the user is hovering on x-values [0:50], it displays "Image1.jpg". If the user is hovering on x-values [51:100], it displays "Image2.jpg". Lastly, if the user is hovering on x-values 101 or greater, it displays "Image3.jpg". These 3 images can be found in the "brain_images" folder.

  Expected output if "main2" is ran correctly:

<img width="959" alt="main2_image1" src="https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/f70370a6-bcca-4037-a5b6-e6d3012ae785">

- Main3.py is similar to main2.py but it displays a different image for every possible x-value a user can hover over (values 0-155). These images are saved in the "MNIST_data" folder which were drawn from the "mini-mnist-1000.pickle" file and converted to jpeg images using code found in the "MNIST_images.ipynb" file.

  Expected output if "main3" is ran correctly:

  <img width="959" alt="main3_image1" src="https://github.com/ShivaniSuthar/VISUALIZATION_TOOLS_UCLA_SU23/assets/122011763/e335b868-052f-434f-b6b5-152f1aa0a1b5">


When incorporating real-patient data, these visualizations can be used to display select patient brain scan images according to a range of x-direction locations in the brain or a specified x-direction location. In addition, the user can manipulate the "random number" variable in the hover textbox to display a desired feature of their choice based on the patient data. Furthermore, deploying the visualizations on Dash aid in their efficiency.                                                         
Lastly, the original code I modified can be found at this link:
https://dash.plotly.com/dash-core-components/tooltip





# How to run the code
In order to run the different code files, first, Docker Desktop must be running since all the code runs using Docker. Then, there are 4 main files involved in running the code - "Dockerfile.demo", "Dockerfile.graphvis", "Dockerfile.slicer", and "run.sh". "Dockerfile.demo" contains the docker script to run "Codefile.py". "Dockerfile.graphvis" contains the docker script to run "app.py". "Dockerfile.slicer" contains the docker script to run either "main.py", "main2.py", or "main3.py". Lastly, "run.sh" contains the bash script to build and run any of the docker files. In order to actually launch the visualizations, open a new bash terminal and type either "bash run.sh demo", "bash run.sh graphvis", or "bash run.sh slicer" depepending on which visualization you want to launch. Finally, to view the visualization, you will have to access the port that was opened specified in the bash terminal. Please note: In order to run "Codefile.py", after running "bash run.sh demo", Ipython will be launched in the terminal and the code contained in "Codefile.py" must be pasted into Ipython and then the visualization will be viewable on the port. In order to run "main.py", "main2.py", or "main3.py", the name of the file you want to run must be updated accordingly in the "Dockerfile.slicer" file in the locations where it says "main_" (3 locations total). The port numbers for the different visualizations can also be updated by changing the port number in the corresponding section in "run.sh" and the corresponding docker file.

