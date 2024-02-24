import argparse

from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from trt_llama_api import TrtLlmAPI
from utils import messages_to_prompt, completion_to_prompt
import json
import logging
import os

# Create an argument parser
parser = argparse.ArgumentParser(description='OutlookLLM Inference Server')

# Add arguments
parser.add_argument('--trt_engine_path', type=str, help="Path to the TensorRT engine.")
parser.add_argument('--trt_engine_name', type=str, help="Name of the TensorRT engine.")
parser.add_argument('--tokenizer_dir_path', type=str, help="Directory path for the tokenizer.")
parser.add_argument('--verbose', type=bool, help="Enable verbose logging.")

parser.add_argument("--host", type=str, help="Set the ip address to listen.(default: 127.0.0.1)")
parser.add_argument("--port", type=int, help="Set the port to listen.(default: 8385)")

parser.add_argument("--max_output_tokens", type=int, help="Maximum output tokens.(default: 2048)")
parser.add_argument("--max_input_tokens", type=int, help="Maximum input tokens.(default: 2048)")
#parser.add_argument("--no_system_prompt", type=bool, help="Skip implicit top system prompt.", default=False)

parser.add_argument('--cert_file', type=str, help="Path to the SSL Cert File.")
parser.add_argument('--cert_key', type=str, help="Path to the SSL Cert File.")

# Parse the arguments
args = parser.parse_args()


def is_present(json, key):
    try:
        buf = json[key]
    except KeyError:
        return False
    if json[key] == None:
        return False
    return True

https_cert_file = ""
https_key_file = ""
trt_engine_path = ""
trt_engine_name = ""
tokenizer_dir_path = ""
verbose = False
host = "127.0.0.1"
port = "8385"
max_output_tokens = 2048
max_input_tokens = 2048

# If a config file is present, config is loaded from file
if os.path.exists("outlookllm_config.json"):
    with open('outlookllm_config.json', 'r') as f:
        config_data = json.load(f)

    https_cert_file = config_data['https_cert_file']
    https_key_file = config_data['https_key_file']
    trt_engine_path = config_data['trt_engine_path']
    trt_engine_name = config_data['trt_engine_name']
    tokenizer_dir_path = config_data['tokenizer_dir_path']
    verbose = config_data['verbose']
    host = config_data['host']
    port = config_data['port']
    max_output_tokens = config_data['max_output_tokens']
    max_input_tokens = config_data['max_input_tokens']


# If arguments are provided in command line, arguments will override config.
if args.trt_engine_path is not None: trt_engine_path = args.trt_engine_path
if args.trt_engine_name is not None: trt_engine_name = args.trt_engine_name
if args.tokenizer_dir_path is not None: tokenizer_dir_path = args.tokenizer_dir_path
if args.verbose is not None: verbose = args.verbose
if args.host is not None: host = args.host
if args.port is not None: port = args.port

if (https_cert_file == "") or (https_key_file  == "") or (trt_engine_path == "") or (trt_engine_name == "") or (tokenizer_dir_path == ""):
     parser.print_help()
     exit()
#no_system_prompt = args.no_system_prompt

app = Flask(__name__)
CORS(app) # to enable CORS from the Add-in

# Configure logging
logging.basicConfig(level=logging.INFO)

# create trt_llm engine object
llm = TrtLlmAPI(
    model_path=trt_engine_path,
    engine_name=trt_engine_name,
    tokenizer_dir=tokenizer_dir_path,
    temperature=0.1,
    max_new_tokens=max_output_tokens,
    context_window=max_input_tokens,
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    verbose=False
)

def completions(prompt, temperature= 1.0, stop_strings = []):
    app.logger.info('llm completion with prompt=%s ', prompt)
    prompt_final = completion_to_prompt(prompt)
    return llm.complete_common(prompt_final, False, temperature=temperature, formatted=True, stop_strings=stop_strings)
    

@app.route('/composeEmail', methods=['POST'])
def composeEmail():
    assert request.headers.get('Content-Type') == 'application/json'
    body = request.get_json()
    
    user_prompt = ""
    if "prompt" in body:
        user_prompt = body["prompt"]

    llm_response = completions(prompt=user_prompt)
    app.logger.info('llm completion response:\n %s ', llm_response)
    response = {'subject':'hello', 'body':'message body'}
    return json.dumps(response)

if __name__ == '__main__':
    # Outlook add-ins can only call URLs under https, here we retrieve the https config and add it to Flask server
    app.run(host, port=port, debug=True, use_reloader=False, threaded=False, ssl_context=(https_cert_file,https_key_file))
