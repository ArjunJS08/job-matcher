from chromadb.utils import embedding_functions

# This uses Chroma's BUILT-IN offline ONNX loader
# It will load from:
# ~/.cache/chroma/onnx_models/all-MiniLM-L6-v2/onnx
# and NEVER hit the internet

_embedding_fn = embedding_functions.ONNXMiniLM_L6_V2()

def embed(text: str) -> list[float]:
    if not text or len(text.strip()) == 0:
        return [0.0] * 384

    return _embedding_fn([text])[0]
