# OutlookLLM ![https://github.com/fgblanch/OutlookLLM/OutlookLLM Add-in/assets/OutlookLLM.png](https://github.com/fgblanch/OutlookLLM/blob/8098168d39ec212007afc4500b0826f054179027/OutlookLLM%20Add-in/assets/OutlookLLM.png) 
Outlook Add-in to use Generative AI features (Email composition, Email Thread Summarization, Inbox Q&amp;A) securely and privately. It uses a local LLM served via Nvidia TensorRT-LLM. 

## Installation and getting started (Windows):

This system has two componentes: 1) An Outlook Add-in front end (React, Office Add-in framework) 2) An LLM inference backend (Python, Flask, TensorRT-LLM)

To get the system running:

1. Clone this [repository](https://github.com/fgblanch/OutlookLLM.git):

   ```
   git clone https://github.com/fgblanch/OutlookLLM.git
   ```
2. Install LLM dependencies:

  2.1 Install [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM/) for Windows using the instructions [here](https://github.com/NVIDIA/TensorRT-LLM/blob/release/0.5.0/windows/README.md).

  2.2 Download or Build your TensorRT-LLM LLM model of choice. The model needs to be Instruct Tuned (Llama format).
     - I used Mistral 7B Intruct tuned from HuggingFace: [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2), and converted to TensorRT-LLM using the instructions [here](https://github.com/NVIDIA/TensorRT-LLM/tree/3c373ebc5b5caf7e41198125131a153f3df08f09/examples/llama)
     - Other models tested are [Llama2 7B HF Chat] (https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) and [Gemma 7b IT](https://huggingface.co/google/gemma-7b-it)

3. Outlook Add-in generation and sideloading.
(WIP)

4. Install LLM Backend dependencies
```
pip install -r requirements.txt
```

5. Configure LLM Backend Https certificates
(WIP)

7. Run LLM Backend
(WIP)

8. Enjoy! ;)

## Next Steps and Roadmap:
- Build RAG on Backend for Inbox and Calendar Q&A
