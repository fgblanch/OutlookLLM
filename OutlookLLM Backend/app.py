import argparse

from flask import Flask, Response, request, jsonify
from trt_llama_api import TrtLlmAPI
from utils import messages_to_prompt, completion_to_prompt
import json
import logging

# Create an argument parser
parser = argparse.ArgumentParser(description='OpenAI Compatible Server')

# Add arguments
parser.add_argument('--trt_engine_path', type=str, required=True,
                    help="Path to the TensorRT engine.", default="")
parser.add_argument('--trt_engine_name', type=str, required=True,
                    help="Name of the TensorRT engine.", default="")
parser.add_argument('--tokenizer_dir_path', type=str, required=True,
                    help="Directory path for the tokenizer.", default="")
parser.add_argument('--verbose', type=bool, required=False,
                    help="Enable verbose logging.", default=False)

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)


slot_id = -1
parser.add_argument("--host", type=str, help="Set the ip address to listen.(default: 127.0.0.1)", default='127.0.0.1')
parser.add_argument("--port", type=int, help="Set the port to listen.(default: 8081)", default=8081)

parser.add_argument("--max_output_tokens", type=int, help="Maximum output tokens.(default: 2048)", default=2048)
parser.add_argument("--max_input_tokens", type=int, help="Maximum input tokens.(default: 2048)", default=2048)
parser.add_argument("--no_system_prompt", type=bool, help="Skip implicit top system prompt.", default=False)

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

# Use the provided arguments
trt_engine_path = args.trt_engine_path
trt_engine_name = args.trt_engine_name
tokenizer_dir_path = args.tokenizer_dir_path
verbose = args.verbose
host = args.host
port = args.port
no_system_prompt = args.no_system_prompt

# create trt_llm engine object
llm = TrtLlmAPI(
    model_path=trt_engine_path,
    engine_name=trt_engine_name,
    tokenizer_dir=tokenizer_dir_path,
    temperature=0.1,
    max_new_tokens=args.max_output_tokens,
    context_window=args.max_input_tokens,
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    verbose=False
)


@app.route('/composeEmail', methods=['POST'])
def composeEmail():
    assert request.headers.get('Content-Type') == 'application/json'
    stream = False
    temperature = 1.0
    body = request.get_json()
    if (is_present(body, "stream")):
        stream = body["stream"]
    if (is_present(body, "temperature")):
        temperature = body["temperature"]

    stop_strings = []
    if is_present(body, "stop"):
        stop_strings = body["stop"]

    if verbose:
        print("/composeEmail called with stream=" + str(stream))

    app.logger.info('/composeEmail called')

    prompt = ""
    if "prompt" in body:
        prompt = body["prompt"]

    app.logger.info('/composeEmail called with prompt=%s ', prompt)

    if not no_system_prompt:
        prompt = completion_to_prompt(prompt)

    formatted = True

    if not stream:
        return llm.complete_common(prompt, False, temperature=temperature, formatted=formatted, stop_strings=stop_strings)
    else:
        return llm.stream_complete_common(prompt, False, temperature=temperature, formatted=formatted, stop_strings=stop_strings)


if __name__ == '__main__':
    
    # Outlook add-ins can only call URLs under https, here we retrieve the https config and add it to Flask server
    with open('outlookllm_config.json', 'r') as f:
        config_data = json.load(f)

    https_cert_file = config_data['https_cert_file']
    https_key_file = config_data['https_key_file']
    
    app.run(host, port=port, debug=True, use_reloader=False, threaded=False, ssl_context=(https_cert_file,https_key_file))
