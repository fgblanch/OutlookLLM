# OutlookLLM ![https://github.com/fgblanch/OutlookLLM/OutlookLLM Add-in/assets/OutlookLLM.png](https://github.com/fgblanch/OutlookLLM/blob/8098168d39ec212007afc4500b0826f054179027/OutlookLLM%20Add-in/assets/OutlookLLM.png) 
Outlook Add-in to use Generative AI features (Email writing, Thread Summarization, Inbox Q&amp;A) securely and privately. It is private and secure by design as it uses a local LLM served via Nvidia TensorRT-LLM. Great for corporate environments.


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
