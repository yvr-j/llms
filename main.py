import openai
import langchain
import os
from dotenv import load_dotenv
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from image import recognize_vegetables
load_dotenv("api.env")

image_url = "https://motionarray.imgix.net/preview-979592-GVfT0W85FOwqemCN-large.jpg?w=1400&q=60&fit=max&auto=format"  # Replace with the URL of your image
vegetable_names = recognize_vegetables(image_url)

if vegetable_names:
    print("Recognized vegetables in the image:")
    for veg in vegetable_names:
        print("-", veg)
else:
    print("No vegetables recognized in the image.")



llm=OpenAI(temperature=0.6)
prompt=PromptTemplate(
  input_variables=["veg",'v','e','g'],
  template="suggest me 5 recipe to cook some dish with help of these vegetable{veg}{v}{e}{g}"
)
chain= LLMChain(llm=llm,prompt=prompt)
output=chain.run(veg="onion",v="tomato",e="capcicum",g="potato")
print(output)
