# Solving Inverse Problems to Generate Synthetic Data

The idea was to use PSLD and knowingly corrupt data to have it be reconstructed by the diffusion model, and in turn, augment the sample. Bounding Boxes of a sample were used to generate masks, where PSLD would then attempt to inpaint. Improved performance on yolov7 object detection model especially in small datasets.
