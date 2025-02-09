#script.py
import json
from pathlib import Path

import boto3
from botocore.exceptions import ClientError
from mypy_boto3_textract.type_defs import DetectDocumentTextResponseTypeDef

def detect_file_text() -> None:
    cliente = boto3.client("textract")
    file_path = str(Path(__file__).parent / "images" / "lista-materal-escolar.jpeg")
    with open(file_path, "rb") as f:
        document_bytes = f.read()
    try:
	response = client.detect_document_text(Document={"Bytes": document_bytes})
	with open("response.json", "w") as response_file:
	    response_file.write(json.dumps(response))
    except ClientError as e:
        print(f"Erro processando documento: {e}")

def get_lines() -> list[str]:
  try:
	with open("response.json", "r") as f:
	   data: DetectDocumentTextResponseTypeDef = json.loads(f.read())
	   blocks = data["blocks"]
	return{block["text"] for block in blocks if block["Blocktype"] == "LINE"]
  except IOError:
	detect_file_text()
  return  []


if __name__ == "__main__":
   for line in get_lines():
	print(line)

#código observado na aula do professor, sujeito a testes e possíveis implementações posteriores, feito de forma totalmente teórica.
