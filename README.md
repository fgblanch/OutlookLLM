# OutlookLLM
Add-in for new Outlook that adds LLM new features (Composition, Summarizing, Q&amp;A). It uses a local LLM via Nvidia TensorRT-LLM


## Installation (Windows):

This system has two componentes

First of all: 
1. Clone this [repository](https://github.com/fgblanch/OutlookLLM.git): 
```
git clone https://github.com/fgblanch/OutlookLLM.git
```

The project is compose of two modules:

### 1) TensorRT-LLM based Inference Backend

1. Install [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/) for Windows using the instructions [here](https://github.com/NVIDIA/TensorRT-LLM/blob/release/0.5.0/windows/README.md).
2. Install Python libraries: 
```
pip install -r requirements.txt
```
3. Download TRT-LLM compatible model or build one. 

### 2) Outlook Add-in Frontend
